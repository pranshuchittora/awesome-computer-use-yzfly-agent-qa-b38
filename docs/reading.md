# 官方文档、博文与参考实现

[返回清单](../README.md) · [选型指南](guide.md) · [远程自动化方案](remote-automation.md)

整理日期：2026-11-06。优先链接项目作者、官方文档和源代码。历史文章用于理解技术演进，安装参数、模型支持和可用性以当前文档为准。

## Claude 与 Anthropic

| 资源 | 类型 | 阅读重点 |
| --- | --- | --- |
| [Developing a computer use model](https://www.anthropic.com/news/developing-computer-use) | 官方博文，2024-10-22 | 电脑操作模型的训练思路、截图到动作的映射，以及当时的局限 |
| [Computer Use Tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) | 当前 API 文档 | 应用如何执行模型请求的截图、点击、输入并回传结果 |
| [Claude Computer Use Demo](https://github.com/anthropics/claude-quickstarts/tree/main/computer-use-demo) | 官方 GitHub 示例 | 把模型 API、桌面容器与工具循环连接起来 |
| [Run Claude Code programmatically](https://code.claude.com/docs/en/headless) | 当前 CLI 文档 | 非交互运行、结构化输出与脚本集成 |
| [Remote Control](https://code.claude.com/docs/en/remote-control) | 当前远程连接文档 | 手机 / Web 继续主机会话、登录要求与进程生命周期 |
| [Claude Agent SDK for Python](https://github.com/anthropics/claude-agent-sdk-python) | 官方 SDK | 把 Agent 循环接入自己的程序 |

## Codex 与 OpenAI

| 资源 | 类型 | 阅读重点 |
| --- | --- | --- |
| [Codex](https://github.com/openai/codex) | 官方 GitHub 仓库 | 终端 Agent 与开发者接口 |
| [Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode) | 当前文档 | `codex exec`、JSONL 与流水线调用 |
| [Scheduled tasks / Automations](https://learn.chatgpt.com/docs/automations) | 当前产品文档 | 周期任务、桌面运行要求与 Web 任务边界 |
| [Computer Use](https://learn.chatgpt.com/docs/computer-use) | 当前产品文档 | 桌面应用操作、系统支持和授权入口 |
| [Remote Connections](https://learn.chatgpt.com/docs/remote-connections) | 当前远程连接文档 | 手机连接主机，以及桌面应用通过 SSH 使用远端项目 |
| [API Computer Use](https://developers.openai.com/api/docs/guides/tools-computer-use) | 当前 API 文档 | 自建环境中的动作执行与截图回传循环 |
| [Codex GitHub Action](https://github.com/openai/codex-action) | 官方 GitHub 项目 | 把 Codex 接入仓库自动化 |

## DeepSeek Harness

| 资源 | 类型 | 阅读重点 |
| --- | --- | --- |
| [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 官方 GitHub 仓库 | 插件式 Agent 运行时和开发者预览状态 |
| [Computer Use 子系统](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/computer-use.md) | 官方源码文档 | 原生 CUA、Cua Driver provider 与执行边界 |
| [Computer Use Bundle](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/experimental/cua-bundle/README.md) | 官方组件文档 | 实验性电脑操作的启用方式 |
| [Claude Code Subagent](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/subagent/subagent-claude-code/README.md) | 官方组件文档 | 委派原生 Claude Code 的会话、返回值与限制 |

## 浏览器、桌面与运行环境

| 资源 | 类型 | 阅读重点 |
| --- | --- | --- |
| [Ego Lite](https://github.com/citrolabs/ego-lite) | 项目 README / Skill | Task Space、登录态、页面快照与 Agent 接入 |
| [Vercel Agent Desktop](https://github.com/vercel-labs/agent-desktop) | 项目 README | 辅助功能树、快照引用、平台边界 |
| [Vercel Agent Browser](https://github.com/vercel-labs/agent-browser) | 项目 README | 浏览器的命令式操作与观察循环 |
| [Playwright CLI](https://github.com/microsoft/playwright-cli) | 官方项目 | CLI + Skills 的浏览器接入方式 |
| [Terminal Mac](https://github.com/govijr/terminal-mac) | 项目 README | 独立虚拟 Mac、客体设置和当前成熟度 |
| [Cua](https://github.com/trycua/cua) | 项目 README | Driver、Lume、Spaces 与组件许可区别 |
| [Gemini Computer Use Preview](https://github.com/google-gemini/computer-use-preview) | 官方示例 | 浏览器后端与模型动作执行 |

## Google 的 CLI 入口

- [Antigravity CLI（agy）](https://antigravity.google/product/antigravity-cli)：终端 Agent 产品，支持插件、技能与子 Agent。
- [Gemini API CLI](https://github.com/google-gemini/gemini-api-cli)：给现有 Agent 和脚本调用模型能力的无状态 API 命令行客户端。
- [Gemini CLI](https://github.com/google-gemini/gemini-cli)：当前上游定位主要为企业 Code Assist 工作流，另保留文档指定的付费 API 路径。
- [官方迁移公告](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)：说明 2026 年个人免费与 Google AI Pro / Ultra 入口迁移到 Antigravity CLI 的安排。

## 评测

- [OSWorld](https://github.com/xlang-ai/OSWorld)：真实桌面环境任务。比较结果时记录基准版本与评分协议。
- [BrowserGym](https://github.com/ServiceNow/BrowserGym)：浏览器 Agent 的统一任务环境。
- [Agent S](https://github.com/simular-ai/Agent-S)：结合可运行框架阅读电脑操作 Agent 的研究演进；上游成绩属于特定实验条件。

## 本清单怎样核验

项目的逐条证据保存在 [data/projects.json](../data/projects.json) 的 `sources`、`checked_at` 和 `verification` 字段。当前所有条目均为 `upstream-docs`：核对公开仓库身份、读取 README 或组件文档，确认描述有依据；并未统一安装、跑分或做横向产品验收。Star 数与营销性能数字不作为自动收录依据。
