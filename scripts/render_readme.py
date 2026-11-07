#!/usr/bin/env python3
"""Validate the curated catalog and render README.md with Python's standard library."""

import argparse
from collections import Counter
from datetime import date, datetime, timezone
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    "desktop": ("桌面操作与 Computer Use", "给 Agent 观察和操作原生应用的能力，包括驱动、完整 Agent 与官方示例。"),
    "browser": ("浏览器与网页自动化", "从共享登录态的浏览器，到适合 Agent 调用的 CLI、MCP 和自动化 SDK。"),
    "harness": ("编码 Agent 与通用 Harness", "负责理解目标、规划步骤、调用工具与管理上下文；具体操作能力来自其工具和扩展。"),
    "tooling": ("Agent 配套：模型、记忆与多会话", "喜鹊、CC Switch、cmux 等配套工具，覆盖模型切换、技能、记忆、终端与并行工作区。"),
    "dsh": ("DeepSeek 与 Claude Code 桥接", "区分官方电脑操作、委派 Claude Code、替换模型路线、迁移配置和复刻交互体验。"),
    "cli": ("适合 Agent 调用的 CLI", "直接操作服务、文件和结构化数据，减少对 GUI 的依赖。"),
    "sandbox": ("虚拟电脑与隔离环境", "给自动化任务提供独立桌面、浏览器或文件环境。运行环境本身不等于完整 Agent。"),
    "remote": ("远程控制与自动化", "从手机指挥 Agent、连接远端主机、持久运行任务到远程桌面接管。具体组合见远程自动化方案。"),
    "mobile": ("手机与模拟器自动化", "覆盖 Android、iOS、真机、模拟器和可复用 UI 测试流程。"),
    "workflow": ("工作流与持续自动化", "把单次任务连接到 CI、事件、调度、重试和结果交付。"),
    "scripting": ("系统脚本与传统自动化", "让 Agent 调用已有的确定性脚本和系统能力。"),
    "benchmark": ("评测与研究环境", "用真实任务与可重复评测判断能力；不把演示视频或不同协议的分数当作统一排名。"),
}


def load_catalog():
    items = json.loads((ROOT / "data/projects.json").read_text(encoding="utf-8"))
    required = {"name", "category", "repository", "github", "interfaces", "platforms", "description", "note", "status", "license", "sources", "checked_at", "verification"}
    seen = set()
    if not isinstance(items, list) or not items:
        raise ValueError("Catalog must be a non-empty list")
    for item in items:
        if not isinstance(item, dict) or set(item) != required:
            raise ValueError(f"Unexpected catalog fields: {item}")
        label = item["name"]
        for key in required - {"interfaces", "sources"}:
            value = item[key]
            if not isinstance(value, str) or (not value and key != "note") or "\n" in value:
                raise ValueError(f"{label}: invalid {key}")
        if item["category"] not in CATEGORIES:
            raise ValueError(f"{label}: unknown category")
        if not re.fullmatch(r"[\w.-]+/[\w.-]+", item["repository"]):
            raise ValueError(f"{label}: invalid repository")
        repo_url = "https://github.com/" + item["repository"]
        if item["github"] != repo_url and not item["github"].startswith(repo_url + "/"):
            raise ValueError(f"{label}: URL does not belong to repository")
        if item["github"].lower() in seen:
            raise ValueError(f"{label}: duplicate URL")
        seen.add(item["github"].lower())
        for key in ("interfaces", "sources"):
            if not isinstance(item[key], list) or not item[key] or not all(isinstance(v, str) and v and "\n" not in v for v in item[key]):
                raise ValueError(f"{label}: invalid {key}")
        if any(not u.startswith("https://") for u in item["sources"]):
            raise ValueError(f"{label}: sources must be HTTPS")
        date.fromisoformat(item["checked_at"])
        if item["verification"] != "upstream-docs":
            raise ValueError(f"{label}: document the new verification level before using it")
    return items


def cell(value):
    return value.replace("|", "\\|")


def load_stars(items):
    snapshot = json.loads((ROOT / "data/github-stars.json").read_text(encoding="utf-8"))
    updated = datetime.fromisoformat(snapshot["updated_at"].replace("Z", "+00:00"))
    if updated.tzinfo is None:
        raise ValueError("Star snapshot timestamp must include a timezone")
    expected = {item["repository"] for item in items}
    if set(snapshot["repositories"]) != expected:
        raise ValueError("Star snapshot does not match catalog; run scripts/update_stars.py")
    for repo, stats in snapshot["repositories"].items():
        if type(stats["stars"]) is not int or stats["stars"] < 0:
            raise ValueError(f"{repo}: invalid Star count")
        if type(stats["archived"]) is not bool:
            raise ValueError(f"{repo}: invalid archive state")
    return snapshot, updated.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def render(items):
    snapshot, star_time = load_stars(items)
    star_counts = {repo: stats["stars"] for repo, stats in snapshot["repositories"].items()}
    total = len(items)
    repos = len({item["repository"].lower() for item in items})
    latest = max(item["checked_at"] for item in items)
    counts = Counter(item["category"] for item in items)
    intro = f"""<!-- Generated from data/projects.json by scripts/render_readme.py. -->
# Awesome Computer Use

**AI 电脑操作与自动化精选：让 Agent 真正完成桌面、浏览器、终端和手机上的任务。**

A curated, Chinese-first collection of computer-use agents, browser automation, CLI tools, sandboxes, and practical resources.

[选型指南](docs/guide.md) · [远程自动化方案](docs/remote-automation.md) · [官方文档与博文](docs/reading.md) · [贡献项目](CONTRIBUTING.md) · [JSON 数据](data/projects.json)

收录 **{total} 个项目与组件 / {repos} 个 GitHub 仓库 / {len(CATEGORIES)} 个分类**。最近整理：**{latest}**。以 GitHub 上游仓库为主，补充必要的官方产品文档和技术文章。

**GitHub Stars：{star_time} 获取的快照**。各分类按 Star 数降序排列；点击数字打开 GitHub Star 页面。同一仓库的组件共享仓库 Star 数，Star 反映关注度，不代表实测质量。[统计数据](data/github-stars.json)

本清单覆盖 **Computer Use + Browser Use + CLI / API Automation**。每个条目说明用途、接口、平台和关键边界；优先选择能找到上游文档、安装入口和明确使用场景的项目。小型但有独特能力的新项目会单独标为“社区探索”或“早期项目”。

> 核验层级：已读取上游 README / 文档并检查仓库身份，**不表示逐项安装实测**。公开 GitHub 仓库不等于产品全部开源；模型、托管服务和不同组件可能使用不同条款。逐条来源、核验日期和许可备注见 [数据清单](data/projects.json)。

## 从这里开始

| 想完成的任务 | 优先查看 | 选择理由 |
| --- | --- | --- |
| 让 Agent 使用已登录的网页，又能继续自己浏览 | [Ego Lite](https://github.com/citrolabs/ego-lite) / [BrowserOS](https://github.com/browseros-ai/BrowserOS) | 专门为人与 Agent 协作设计的浏览器 |
| 让 Codex / Claude Code 从 shell 操作网页 | [Agent Browser](https://github.com/vercel-labs/agent-browser) / [Playwright CLI](https://github.com/microsoft/playwright-cli) | 可组合的命令接口和页面状态观察 |
| 操作原生桌面应用 | [Agent Desktop](https://github.com/vercel-labs/agent-desktop) / [Cua Driver](https://github.com/trycua/cua/tree/main/libs/cua-driver) | 辅助功能、窗口和元素操作接口 |
| 用 Mac 做桌面自动化 | [Peekaboo](https://github.com/openclaw/Peekaboo) / [Open Computer Use](https://github.com/iFurySt/open-computer-use) | CLI / MCP 接入已有 Agent |
| 给 Agent 一台独立虚拟 Mac | [Terminal Mac](https://github.com/govijr/terminal-mac) / [Cua](https://github.com/trycua/cua) | 独立桌面；注意客体首次设置与组件成熟度 |
| 把代码或文件任务放进脚本 / CI | [Codex](https://github.com/openai/codex) / [Claude Code](https://github.com/anthropics/claude-code) | 非交互模式与可程序化工具调用 |
| 集中管理 Agent 的模型与配置 | [喜鹊 Magpie](https://github.com/yetone/magpie) / [CC Switch](https://github.com/farion1231/cc-switch) | 模型接入、配置切换和工具资源管理 |
| 管理多个 Agent 会话与工作区 | [cmux](https://github.com/manaflow-ai/cmux) / [Paradev](https://github.com/ParadevAI/Paradev) | 终端、通知、独立工作区与任务观察 |
| 从手机或聊天软件远程下达任务 | [Happy](https://github.com/slopus/happy) / [HAPI](https://github.com/tiann/hapi) / [cc-connect](https://github.com/chenhg5/cc-connect) | 远程继续会话、查看结果与处理审批 |
| 操作远端电脑或云环境 | [远程自动化方案](docs/remote-automation.md) | SSH、私有网络、远端驱动、云浏览器与人工接管的组合 |
| 用 DeepSeek 操作电脑或组合 Claude Code | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) / [桥接分类](#dsh) | 官方 provider 与不同桥接方式分开说明 |
| 处理 GitHub、Google Workspace、云盘与文档 | [CLI 分类](#cli) | 直接使用结构化接口，便于批量处理与验证 |
| 操作手机或回归测试 App | [Mobile MCP](https://github.com/mobile-next/mobile-mcp) / [Maestro](https://github.com/mobile-dev-inc/Maestro) | 连接设备、操作界面、验证结果 |

## 目录

"""
    parts = [intro]
    for slug, (title, _) in CATEGORIES.items():
        parts.append(f"- [{title}](#{slug})（{counts[slug]}）\n")
    parts.append("- [官方产品与阅读入口](#official-resources)\n- [如何贡献](#contributing)\n")
    for slug, (title, description) in CATEGORIES.items():
        parts.append(f'\n<a id="{slug}"></a>\n\n## {title}\n\n{description}\n\n')
        parts.append("| 项目 | Stars | 接口 / 平台 | 适用场景 | 状态与边界 |\n| --- | ---: | --- | --- | --- |\n")
        members = sorted((i for i in items if i["category"] == slug), key=lambda i: (-star_counts[i["repository"]], i["name"].casefold()))
        for item in members:
            interface = "、".join(item["interfaces"]) + "；" + item["platforms"]
            status = ("**" + item["status"] + "** · ") if item["status"] != "项目" else ""
            stars = f"[{star_counts[item['repository']]:,}](https://github.com/{item['repository']}/stargazers)"
            parts.append(f"| [{cell(item['name'])}]({item['github']}) | {stars} | {cell(interface)} | {cell(item['description'])} | {cell(status + item['note'])} |\n")
    parts.append("""
<a id="official-resources"></a>

## 官方产品与阅读入口

这些资源不以是否有完整源码仓库作为收录前提，单独列出，避免与 GitHub 工具混淆。

| 资源 | 值得看的内容 |
| --- | --- |
| [Codex / ChatGPT Computer Use](https://learn.chatgpt.com/docs/computer-use) | 桌面产品的电脑操作能力；按地区、系统和账户实际开放情况使用 |
| [Codex 非交互模式](https://learn.chatgpt.com/docs/non-interactive-mode) | `codex exec`、机器可读输出和脚本集成 |
| [定时任务 / Automations](https://learn.chatgpt.com/docs/automations) | 区分桌面本地任务与 Web 任务；使用本地文件时需要电脑和应用保持运行 |
| [Claude：Developing a computer use model](https://www.anthropic.com/news/developing-computer-use) | 2024 年原始技术博文，解释截图、动作与模型训练思路；历史评测不当作当前成绩 |
| [Claude Computer Use Tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) | 当前 API 工具与客户端动作循环 |
| [Claude Code 程序化运行](https://code.claude.com/docs/en/headless) | `claude -p` 与 SDK 自动化入口 |
| [DeepSeek Computer Use 文档](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/computer-use.md) | 官方实现、provider、权限与执行边界 |
| [OpenAI API Computer Use](https://developers.openai.com/api/docs/guides/tools-computer-use) | 自己实现观察、动作执行和结果回传的 API 接入方式 |
| [Antigravity CLI（agy）](https://antigravity.google/product/antigravity-cli) | Google 的终端 Agent 产品，支持 Skills、Hooks、MCP 与子 Agent；与 Gemini API CLI 区分 |
| [Codex Remote Connections](https://learn.chatgpt.com/docs/remote-connections) | 从手机继续主机任务，或让桌面应用通过 SSH 使用远端项目 |
| [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control) | 从手机或浏览器继续本机运行的 Claude Code 会话 |

进一步阅读：[官方文档与博文](docs/reading.md)。实际搭配：[选型指南](docs/guide.md) · [远程自动化方案](docs/remote-automation.md)。

<a id="contributing"></a>

## 如何贡献

欢迎补充能解决真实问题的项目、纠正能力描述或报告失效链接。请提供上游仓库、具体使用场景、接口、平台和证据；商业产品、官方示例、社区项目与实验性能力要写清楚。

修改 `data/projects.json` 后运行：

```bash
python3 scripts/update_stars.py
python3 scripts/render_readme.py
python3 scripts/render_readme.py --check
```

`update_stars.py` 使用已登录的 GitHub CLI 获取全部仓库的当前 Star 数；获取失败时保留旧快照。详细规则见 [CONTRIBUTING.md](CONTRIBUTING.md)。本项目不按 Star 数自动收录，也不把未经实测的条目标为实测推荐。

相关清单：[Awesome MCP ZH](https://github.com/yzfly/Awesome-MCP-ZH) · [Awesome DSH Skills](https://github.com/yzfly/awesome-dsh-skills)。

## 许可

本仓库的原创整理内容和维护脚本使用 [MIT License](LICENSE)。被收录项目、商标、模型和服务遵循各自上游条款。
""")
    return "".join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check catalog and README without writing files")
    args = parser.parse_args()
    try:
        items = load_catalog()
        result = render(items)
        target = ROOT / "README.md"
        if args.check:
            if not target.exists() or target.read_text(encoding="utf-8") != result:
                raise ValueError("README is stale; run python3 scripts/render_readme.py")
        else:
            target.write_text(result, encoding="utf-8")
        print(f"OK: {len(items)} entries, {len({i['repository'].lower() for i in items})} repositories")
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
