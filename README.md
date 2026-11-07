<!-- Generated from data/projects.json by scripts/render_readme.py. -->
# Awesome Computer Use

**AI 电脑操作与自动化精选：让 Agent 真正完成桌面、浏览器、终端和手机上的任务。**

A curated, Chinese-first collection of computer-use agents, browser automation, CLI tools, sandboxes, and practical resources.

[选型指南](docs/guide.md) · [远程自动化方案](docs/remote-automation.md) · [官方文档与博文](docs/reading.md) · [贡献项目](CONTRIBUTING.md) · [JSON 数据](data/projects.json)

收录 **106 个项目与组件 / 103 个 GitHub 仓库 / 12 个分类**。最近整理：**2026-11-07**。以 GitHub 上游仓库为主，补充必要的官方产品文档和技术文章。

**GitHub Stars 使用 [Shields.io 动态徽章](https://shields.io/badges/git-hub-repo-stars)**，点击徽章查看仓库 Star 页面；数值自动更新，可能有缓存延迟。各分类按最近整理时的 Star 数据排序，顺序不随徽章自动变化。同一仓库的组件共享仓库 Star 数，Star 反映关注度，不代表实测质量。

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

- [桌面操作与 Computer Use](#desktop)（11）
- [浏览器与网页自动化](#browser)（17）
- [编码 Agent 与通用 Harness](#harness)（15）
- [Agent 配套：模型、记忆与多会话](#tooling)（9）
- [DeepSeek 与 Claude Code 桥接](#dsh)（5）
- [适合 Agent 调用的 CLI](#cli)（12）
- [虚拟电脑与隔离环境](#sandbox)（8）
- [远程控制与自动化](#remote)（11）
- [手机与模拟器自动化](#mobile)（7）
- [工作流与持续自动化](#workflow)（6）
- [系统脚本与传统自动化](#scripting)（3）
- [评测与研究环境](#benchmark)（2）
- [官方产品与阅读入口](#official-resources)
- [如何贡献](#contributing)

<a id="desktop"></a>

## 桌面操作与 Computer Use

给 Agent 观察和操作原生应用的能力，包括驱动、完整 Agent 与官方示例。

| 项目 | Stars | 接口 / 平台 | 适用场景 | 状态与边界 |
| --- | ---: | --- | --- | --- |
| [UI-TARS Desktop / Agent TARS](https://github.com/bytedance/UI-TARS-desktop) | [![GitHub Stars](https://img.shields.io/github/stars/bytedance/UI-TARS-desktop?style=social)](https://github.com/bytedance/UI-TARS-desktop/stargazers) | App、CLI、Web UI；桌面 / 浏览器 | 字节跳动的多模态 Agent 项目，包含桌面操作应用与 Agent TARS 工具链。 | 本地、远程和浏览器模式的要求不同；模型需要另行配置。 |
| [Cua Driver](https://github.com/trycua/cua/tree/main/libs/cua-driver) | [![GitHub Stars](https://img.shields.io/github/stars/trycua/cua?style=social)](https://github.com/trycua/cua/stargazers) | CLI、MCP、SDK；macOS / Windows / Linux | 为 Agent 提供原生应用、窗口、元素和输入控制接口。 | 与 Cua Spaces 分开选型；后台输入有平台与应用限制。 |
| [OmniParser / OmniTool](https://github.com/microsoft/OmniParser) | [![GitHub Stars](https://img.shields.io/github/stars/microsoft/OmniParser?style=social)](https://github.com/microsoft/OmniParser/stargazers) | Python、模型；截图解析；Windows VM 示例 | 把界面截图解析为可交互区域，辅助视觉 Agent 定位控件。 | 解析器本身不等于完整 Agent；模型权重与代码许可须分别查看。 |
| [Claude Computer Use Demo](https://github.com/anthropics/claude-quickstarts/tree/main/computer-use-demo) | [![GitHub Stars](https://img.shields.io/github/stars/anthropics/claude-quickstarts?style=social)](https://github.com/anthropics/claude-quickstarts/stargazers) | Python、Docker；Linux 桌面容器 | Anthropic 官方参考实现，演示截图、动作执行、工具结果与模型循环。 | **官方示例** · 示例工程；需要模型 API 与运行环境。 |
| [Vercel Agent Desktop](https://github.com/vercel-labs/agent-desktop) | [![GitHub Stars](https://img.shields.io/github/stars/vercel-labs/agent-desktop?style=social)](https://github.com/vercel-labs/agent-desktop/stargazers) | CLI、MCP、C SDK；macOS / Windows / Linux | 通过系统辅助功能树读取桌面、返回元素引用并操作原生应用。 | 不内置模型；后台操作范围取决于应用与平台。 |
| [Agent S](https://github.com/simular-ai/Agent-S) | [![GitHub Stars](https://img.shields.io/github/stars/simular-ai/Agent-S?style=social)](https://github.com/simular-ai/Agent-S/stargazers) | Python、CLI；macOS / Windows / Linux | Simular 的通用电脑操作 Agent 框架，结合任务规划与 GUI 操作。 | 偏研发和实验；不同版本、模型与评测协议不能直接横比。 |
| [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | [![GitHub Stars](https://img.shields.io/github/stars/CursorTouch/Windows-MCP?style=social)](https://github.com/CursorTouch/Windows-MCP/stargazers) | MCP；Windows | 通过 Windows UI 状态、键鼠和应用控制，让 Agent 操作本机桌面。 | 视觉模型并非必需；当前 Python 与 Windows 版本要求见安装文档。 |
| [Microsoft UFO](https://github.com/microsoft/UFO) | [![GitHub Stars](https://img.shields.io/github/stars/microsoft/UFO?style=social)](https://github.com/microsoft/UFO/stargazers) | Python、Agent；Windows；多设备扩展 | 包含 Windows 桌面 AgentOS 与跨设备任务编排，结合 GUI 和应用 API。 | UFO² 与 UFO³ 的目标不同，应按单机或多设备场景选择。 |
| [Peekaboo](https://github.com/openclaw/Peekaboo) | [![GitHub Stars](https://img.shields.io/github/stars/openclaw/Peekaboo?style=social)](https://github.com/openclaw/Peekaboo/stargazers) | CLI、MCP、App；macOS | 结合截图、辅助功能检查和原生 UI 操作，适合 Mac 桌面自动化。 | 当前发行版要求 macOS 15+；需相应系统权限。 |
| [Gemini Computer Use Preview](https://github.com/google-gemini/computer-use-preview) | [![GitHub Stars](https://img.shields.io/github/stars/google-gemini/computer-use-preview?style=social)](https://github.com/google-gemini/computer-use-preview/stargazers) | Python、CLI；浏览器 | Google 官方电脑操作示例，以 Playwright 等后端执行模型动作。 | **官方示例** · 预览示例；主要展示浏览器任务，不能据此推断任意桌面应用支持。 |
| [Open Computer Use](https://github.com/iFurySt/open-computer-use) | [![GitHub Stars](https://img.shields.io/github/stars/iFurySt/open-computer-use?style=social)](https://github.com/iFurySt/open-computer-use/stargazers) | CLI、MCP、Skill；macOS / Windows / Linux | 把桌面观察与操作封装为 MCP 服务，可接入 Codex、Claude Code 等。 | 社区实现；平台支持细节和系统权限见上游。 |

<a id="browser"></a>

## 浏览器与网页自动化

从共享登录态的浏览器，到适合 Agent 调用的 CLI、MCP 和自动化 SDK。

| 项目 | Stars | 接口 / 平台 | 适用场景 | 状态与边界 |
| --- | ---: | --- | --- | --- |
| [Firecrawl](https://github.com/firecrawl/firecrawl) | [![GitHub Stars](https://img.shields.io/github/stars/firecrawl/firecrawl?style=social)](https://github.com/firecrawl/firecrawl/stargazers) | API、SDK、MCP；Web；自托管或云端 | 搜索、采集、解析和交互网页，为 Agent 提供 Markdown、JSON 与截图。 | 规范仓库为 firecrawl/firecrawl；托管服务与自托管能力分开评估。 |
| [Browser Use](https://github.com/browser-use/browser-use) | [![GitHub Stars](https://img.shields.io/github/stars/browser-use/browser-use?style=social)](https://github.com/browser-use/browser-use/stargazers) | Python、TypeScript、CLI；浏览器；本地或云端 | 把模型与浏览器操作结合，构建网页任务 Agent；提供本地库与云端服务。 | 开源代码与托管浏览器、托管 Agent 服务分开看。 |
| [Playwright](https://github.com/microsoft/playwright) | [![GitHub Stars](https://img.shields.io/github/stars/microsoft/playwright?style=social)](https://github.com/microsoft/playwright/stargazers) | SDK、CLI；Chromium / Firefox / WebKit | 成熟的浏览器自动化底座，适合把已确认流程固化为可重复脚本。 | **基础工具** · 本身不负责自然语言规划。 |
| [Puppeteer](https://github.com/puppeteer/puppeteer) | [![GitHub Stars](https://img.shields.io/github/stars/puppeteer/puppeteer?style=social)](https://github.com/puppeteer/puppeteer/stargazers) | JavaScript API；Chrome / Firefox | 通过程序控制浏览器，完成页面交互、截图、PDF 与采集任务。 | **基础工具** · 适合明确的脚本流程和自建 Agent 工具。 |
| [Chrome DevTools for Agents](https://github.com/ChromeDevTools/chrome-devtools-mcp) | [![GitHub Stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=social)](https://github.com/ChromeDevTools/chrome-devtools-mcp/stargazers) | MCP、CLI；Chrome | 让 Agent 检查网页、网络、控制台和性能，同时执行页面自动化。 | 更适合网页调试和验收；不负责操作所有桌面应用。 |
| [Vercel Agent Browser](https://github.com/vercel-labs/agent-browser) | [![GitHub Stars](https://img.shields.io/github/stars/vercel-labs/agent-browser?style=social)](https://github.com/vercel-labs/agent-browser/stargazers) | CLI、Skill；macOS / Windows / Linux | 把网页快照和元素引用交给 Agent，通过短命令完成导航与交互。 | 页面变化后需要重新观察；与 Agent Desktop 是不同项目。 |
| [Lightpanda](https://github.com/lightpanda-io/browser) | [![GitHub Stars](https://img.shields.io/github/stars/lightpanda-io/browser?style=social)](https://github.com/lightpanda-io/browser/stargazers) | CLI、CDP、MCP；Linux / macOS | 面向自动化的轻量无头浏览器，执行 DOM 与 JavaScript 网页任务。 | 浏览器兼容性应按目标站点验证；不作为像素渲染验收工具。 |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | [![GitHub Stars](https://img.shields.io/github/stars/microsoft/playwright-mcp?style=social)](https://github.com/microsoft/playwright-mcp/stargazers) | MCP；macOS / Windows / Linux | Microsoft 的 Playwright MCP 服务，提供结构化页面观察和浏览器操作。 | 适合通过 MCP 接入；仍需准备浏览器运行环境。 |
| [Selenium](https://github.com/SeleniumHQ/selenium) | [![GitHub Stars](https://img.shields.io/github/stars/SeleniumHQ/selenium?style=social)](https://github.com/SeleniumHQ/selenium/stargazers) | WebDriver、SDK；多浏览器 | 跨浏览器自动化生态，适合接入已有测试设施和远程浏览器集群。 | **基础工具** · 已有 WebDriver 流程可作为 Agent 的执行后端。 |
| [Page Agent](https://github.com/alibaba/page-agent) | [![GitHub Stars](https://img.shields.io/github/stars/alibaba/page-agent?style=social)](https://github.com/alibaba/page-agent/stargazers) | JavaScript、浏览器扩展；网页内部 | 在网页中嵌入自然语言 GUI Agent，适合给已有 Web 产品增加操作助手。 | 网页内能力有明确边界；不等于全系统电脑操作。 |
| [Stagehand](https://github.com/browserbase/stagehand) | [![GitHub Stars](https://img.shields.io/github/stars/browserbase/stagehand?style=social)](https://github.com/browserbase/stagehand/stargazers) | SDK；浏览器；本地或云端 | 用 act、observe、extract 等接口组织网页操作和结构化信息提取。 | 适合将 AI 动作嵌入代码；需配置模型与浏览器。 |
| [Skyvern](https://github.com/Skyvern-AI/skyvern) | [![GitHub Stars](https://img.shields.io/github/stars/Skyvern-AI/skyvern?style=social)](https://github.com/Skyvern-AI/skyvern/stargazers) | SDK、API、Web UI；浏览器；自托管或云端 | 结合视觉模型与浏览器操作，编排表单、后台系统等业务流程。 | 自托管软件与商业托管服务分开评估。 |
| [Ego Lite / ego-browser](https://github.com/citrolabs/ego-lite) | [![GitHub Stars](https://img.shields.io/github/stars/citrolabs/ego-lite?style=social)](https://github.com/citrolabs/ego-lite/stargazers) | Skill、JavaScript、CLI；macOS / Windows | 面向人与 Agent 协作的浏览器；在独立 Space 中使用页面快照、点击与填表。 | 使用 Ego Lite 中的登录状态；公开仓库的许可不代表全部浏览器发行组件。 |
| [Midscene.js](https://github.com/web-infra-dev/midscene) | [![GitHub Stars](https://img.shields.io/github/stars/web-infra-dev/midscene?style=social)](https://github.com/web-infra-dev/midscene/stargazers) | JavaScript、YAML、CLI；Web / Android / iOS / 桌面 | 用自然语言描述界面操作和断言，执行视觉驱动的端到端测试。 | 不同目标需要对应适配器与运行环境。 |
| [Playwright CLI](https://github.com/microsoft/playwright-cli) | [![GitHub Stars](https://img.shields.io/github/stars/microsoft/playwright-cli?style=social)](https://github.com/microsoft/playwright-cli/stargazers) | CLI、Skill；macOS / Windows / Linux | 为编码 Agent 提供 Playwright 命令接口，支持页面操作、截图和会话。 | 适合已有 shell 能力的 Agent；与 Playwright MCP 分开使用。 |
| [BrowserOS](https://github.com/browseros-ai/BrowserOS) | [![GitHub Stars](https://img.shields.io/github/stars/browseros-ai/BrowserOS?style=social)](https://github.com/browseros-ai/BrowserOS/stargazers) | App、MCP；macOS / Windows / Linux | 给外部 Agent 使用的独立浏览器，支持导入登录状态、并行标签和操作回放。 | 核验时主推 BrowserOS neo；需区分新旧产品文档。 |
| [Nanobrowser](https://github.com/nanobrowser/nanobrowser) | [![GitHub Stars](https://img.shields.io/github/stars/nanobrowser/nanobrowser?style=social)](https://github.com/nanobrowser/nanobrowser/stargazers) | 浏览器扩展；Chrome | 在现有浏览器中用侧栏 Agent 执行网页任务，复用浏览器会话。 | 需要配置支持的模型；操作范围与扩展权限相关。 |

<a id="harness"></a>

## 编码 Agent 与通用 Harness

负责理解目标、规划步骤、调用工具与管理上下文；具体操作能力来自其工具和扩展。

| 项目 | Stars | 接口 / 平台 | 适用场景 | 状态与边界 |
| --- | ---: | --- | --- | --- |
| [OpenClaw](https://github.com/openclaw/openclaw) | [![GitHub Stars](https://img.shields.io/github/stars/openclaw/openclaw?style=social)](https://github.com/openclaw/openclaw/stargazers) | Gateway、CLI、插件；多平台 | 自托管个人助手，通过消息渠道、模型插件和工具连接持续工作流。 | 电脑控制需要相应节点或驱动；不是单独一个鼠标点击库。 |
| [DeepSeek Harness（DSH）](https://github.com/deepseek-ai/deepseek-harness) | [![GitHub Stars](https://img.shields.io/github/stars/deepseek-ai/deepseek-harness?style=social)](https://github.com/deepseek-ai/deepseek-harness/stargazers) | CLI、Web UI、插件；本地；依插件平台支持 | DeepSeek 官方插件式 Agent 运行时，提供工具、会话、子 Agent 与可组合能力。 | **开发者预览** · 电脑操作需选择并启用对应 provider；版本迭代可能有不兼容变更。 |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | [![GitHub Stars](https://img.shields.io/github/stars/NousResearch/hermes-agent?style=social)](https://github.com/NousResearch/hermes-agent/stargazers) | CLI、Gateway、Skills；本地 / SSH / 容器 / 云端 | 结合记忆、技能、聊天渠道与定时任务的通用 Agent，支持多种远端执行后端。 | 电脑操作需对应工具；可在远端常驻，通过聊天渠道下达任务。 |
| [OpenCode](https://github.com/anomalyco/opencode) | [![GitHub Stars](https://img.shields.io/github/stars/anomalyco/opencode?style=social)](https://github.com/anomalyco/opencode/stargazers) | CLI、SDK、服务端；本地开发环境 | 支持多模型的编码 Agent，适合搭配自定义工具和服务接口。 | 模型、权限及工具能力由具体配置决定。 |
| [Claude Code](https://github.com/anthropics/claude-code) | [![GitHub Stars](https://img.shields.io/github/stars/anthropics/claude-code?style=social)](https://github.com/anthropics/claude-code/stargazers) | CLI、Hooks、MCP；macOS / Windows / Linux | 通过 claude -p、Hooks 和 MCP 构建代码、文件与工具自动化。 | 公开仓库用于文档、反馈与扩展；勿据此称产品本体为开源。 |
| [Codex](https://github.com/openai/codex) | [![GitHub Stars](https://img.shields.io/github/stars/openai/codex?style=social)](https://github.com/openai/codex/stargazers) | CLI、SDK、App Server；本地开发环境 / CI | 用 codex exec 执行非交互任务，把代码、文件与工具调用接入脚本流程。 | CLI、桌面 Computer Use 与定时任务是不同入口，详见选型指南。 |
| [Pi](https://github.com/earendil-works/pi) | [![GitHub Stars](https://img.shields.io/github/stars/earendil-works/pi?style=social)](https://github.com/earendil-works/pi/stargazers) | CLI、JSON、RPC、SDK；macOS / Windows / Linux | 可扩展的轻量 Agent Harness，支持脚本模式、RPC、技能与扩展。 | 使用当前仓库 earendil-works/pi；按所需能力自行组合扩展。 |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | [![GitHub Stars](https://img.shields.io/github/stars/google-gemini/gemini-cli?style=social)](https://github.com/google-gemini/gemini-cli/stargazers) | CLI、MCP、扩展；本地开发环境 | Google 维护的开源终端 Agent，当前主要面向企业 Code Assist 工作流。 | 个人免费及 Google AI Pro / Ultra 入口已迁至 Antigravity CLI；付费 API 路径见上游。 |
| [OpenHands / Agent Canvas](https://github.com/OpenHands/OpenHands) | [![GitHub Stars](https://img.shields.io/github/stars/OpenHands/OpenHands?style=social)](https://github.com/OpenHands/OpenHands/stargazers) | Web UI、Agent、后端接口；本地 / 远端 / 云端 | 自托管 Agent 工作台，连接编码 Agent、隔离执行后端和持续自动化任务。 | 内置 Agent 与第三方 ACP Agent 的接入方式不同。 |
| [Cline](https://github.com/cline/cline) | [![GitHub Stars](https://img.shields.io/github/stars/cline/cline?style=social)](https://github.com/cline/cline/stargazers) | IDE、CLI、App、SDK；依入口；桌面与 CI | 组合文件、命令、浏览器和 MCP 工具的 Agent，支持无头脚本与应用集成。 | IDE 扩展、桌面应用、SDK 和 CLI 的运行要求分别查看。 |
| [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | [![GitHub Stars](https://img.shields.io/github/stars/openinterpreter/openinterpreter?style=social)](https://github.com/openinterpreter/openinterpreter/stargazers) | CLI、ACP；macOS / Windows / Linux | 面向开放及低成本模型的编码 Agent，提供可切换的 Harness 行为。 | 当前仓库为 openinterpreter/openinterpreter；不要沿用旧 Python 版能力描述。 |
| [Goose](https://github.com/aaif-goose/goose) | [![GitHub Stars](https://img.shields.io/github/stars/aaif-goose/goose?style=social)](https://github.com/aaif-goose/goose/stargazers) | App、CLI、API、MCP；macOS / Windows / Linux | 可扩展的通用 Agent，用于编码、研究、文件处理与工作流自动化。 | 当前规范仓库为 aaif-goose/goose；工具能力由扩展提供。 |
| [nanobot](https://github.com/HKUDS/nanobot) | [![GitHub Stars](https://img.shields.io/github/stars/HKUDS/nanobot?style=social)](https://github.com/HKUDS/nanobot/stargazers) | Python、CLI、Web UI、Gateway；本地 / 自托管服务器 | 轻量个人 Agent，通过聊天渠道操作文件、保存记忆并调度任务。 | 适合个人远程助手；能力依赖模型与已配置工具。 |
| [Qwen Code](https://github.com/QwenLM/qwen-code) | [![GitHub Stars](https://img.shields.io/github/stars/QwenLM/qwen-code?style=social)](https://github.com/QwenLM/qwen-code/stargazers) | CLI、MCP；本地开发环境 | Qwen 的开源终端编码 Agent，用于代码修改和工具驱动的任务流程。 | GUI 操作需要额外执行工具。 |
| [Claude Agent SDK（Python）](https://github.com/anthropics/claude-agent-sdk-python) | [![GitHub Stars](https://img.shields.io/github/stars/anthropics/claude-agent-sdk-python?style=social)](https://github.com/anthropics/claude-agent-sdk-python/stargazers) | Python SDK；Python 环境 | 把 Claude Code 的 Agent 循环和工具能力嵌入应用与自动化服务。 | SDK 许可与随附 Claude Code 运行时条款分开看。 |

<a id="tooling"></a>

## Agent 配套：模型、记忆与多会话

喜鹊、CC Switch、cmux 等配套工具，覆盖模型切换、技能、记忆、终端与并行工作区。

| 项目 | Stars | 接口 / 平台 | 适用场景 | 状态与边界 |
| --- | ---: | --- | --- | --- |
| [Superpowers](https://github.com/obra/superpowers) | [![GitHub Stars](https://img.shields.io/github/stars/obra/superpowers?style=social)](https://github.com/obra/superpowers/stargazers) | Skills、插件；多种编码 Agent | 把需求澄清、计划、实现与验证组织为可组合的 Agent 工作方法和技能。 | 属于任务方法与技能层；执行工具仍由宿主 Agent 提供。 |
| [CC Switch](https://github.com/farion1231/cc-switch) | [![GitHub Stars](https://img.shields.io/github/stars/farion1231/cc-switch?style=social)](https://github.com/farion1231/cc-switch/stargazers) | App、本地代理；macOS / Windows / Linux | 集中管理 Claude Code、Codex、OpenCode、DSH 等工具的供应商和配置。 | 适合多个 Agent 共用模型服务的工作流；按上游说明处理配置备份与切换。 |
| [Claude-Mem](https://github.com/thedotmack/claude-mem) | [![GitHub Stars](https://img.shields.io/github/stars/thedotmack/claude-mem?style=social)](https://github.com/thedotmack/claude-mem/stargazers) | 插件、CLI、MCP；支持的 Agent 宿主 | 记录、压缩和检索会话中的工作信息，为后续任务提供持久上下文。 | 不同 Agent 的采集与检索支持不同；部分接入仅提供记忆搜索。 |
| [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | [![GitHub Stars](https://img.shields.io/github/stars/router-for-me/CLIProxyAPI?style=social)](https://github.com/router-for-me/CLIProxyAPI/stargazers) | HTTP API、代理服务；本地 / 服务器 | 为支持的模型与 CLI 后端提供兼容 API，连接不同协议的 Agent 客户端。 | 属于接入与协议适配层；各提供商的支持方式和授权要求见上游。 |
| [喜鹊 Magpie](https://github.com/yetone/magpie) | [![GitHub Stars](https://img.shields.io/github/stars/yetone/magpie?style=social)](https://github.com/yetone/magpie/stargazers) | App、CLI、本地网关；macOS / Windows / Linux 等 | 统一管理多个 Agent 的模型、供应商、配置和工具资源，通过本地网关切换模型路线。 | 具体代理、模型与平台能力按上游支持表配置；不内置桌面动作驱动。 |
| [cmux](https://github.com/manaflow-ai/cmux) | [![GitHub Stars](https://img.shields.io/github/stars/manaflow-ai/cmux?style=social)](https://github.com/manaflow-ai/cmux/stargazers) | App、CLI、Socket API；macOS | 面向编码 Agent 的终端工作台，组合多会话、通知、可编程浏览器和 SSH 工作区。 | 基于 Ghostty；适合管理本地与远端任务。 |
| [Paradev（原 Superset）](https://github.com/ParadevAI/Paradev) | [![GitHub Stars](https://img.shields.io/github/stars/ParadevAI/Paradev?style=social)](https://github.com/ParadevAI/Paradev/stargazers) | App、CLI；macOS；Linux 实验版 | 在独立 Git worktree 中并行运行 CLI Agent，集中管理终端、代码审查和浏览器预览。 | 远程主机和自动化等功能按套餐开放；当前规范仓库为 ParadevAI/Paradev。 |
| [Worktrunk](https://github.com/max-sixty/worktrunk) | [![GitHub Stars](https://img.shields.io/github/stars/max-sixty/worktrunk?style=social)](https://github.com/max-sixty/worktrunk/stargazers) | CLI、Hooks；Git 工作区 | 简化 Git worktree 的创建、切换与清理，为并行 Agent 任务提供独立工作目录。 | 适合代码任务隔离；worktree 不等同于系统级沙箱。 |
| [GSD Core（Get Shit Done）](https://github.com/open-gsd/gsd-core) | [![GitHub Stars](https://img.shields.io/github/stars/open-gsd/gsd-core?style=social)](https://github.com/open-gsd/gsd-core/stargazers) | CLI、Skills、工作流；多种编码 Agent | 用需求、阶段计划与上下文管理组织较长的编码任务。 | 旧仓库 gsd-build/get-shit-done 已归档；此处 Star 统计来自当前仓库。 |

<a id="dsh"></a>

## DeepSeek 与 Claude Code 桥接

区分官方电脑操作、委派 Claude Code、替换模型路线、迁移配置和复刻交互体验。

| 项目 | Stars | 接口 / 平台 | 适用场景 | 状态与边界 |
| --- | ---: | --- | --- | --- |
| [DSH Claude Code Subagent](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/subagent/subagent-claude-code) | [![GitHub Stars](https://img.shields.io/github/stars/deepseek-ai/deepseek-harness?style=social)](https://github.com/deepseek-ai/deepseek-harness/stargazers) | DSH 插件；依 Claude Code 运行环境 | DSH 官方插件，把自包含任务委派给原生 Claude Code 会话。 | **官方组件** · 返回最终答案或失败诊断；不是把完整交互过程透明搬进 DSH。 |
| [DSH Computer Use](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/computer-use.md) | [![GitHub Stars](https://img.shields.io/github/stars/deepseek-ai/deepseek-harness?style=social)](https://github.com/deepseek-ai/deepseek-harness/stargazers) | 原生 provider、MCP provider；macOS 原生 CUA；其他依 provider | 官方桌面观察与操作能力，包含原生 CUA 和 Cua Driver 集成。 | **官方实验性** · 实验性、显式启用；同一 composition 仅注册一个 provider。 |
| [DSH Bridges](https://github.com/yhlooo/dsh-bridges) | [![GitHub Stars](https://img.shields.io/github/stars/yhlooo/dsh-bridges?style=social)](https://github.com/yhlooo/dsh-bridges/stargazers) | DSH 插件；依所桥接 Harness | 将 Claude Code、Codex 等已有配置与部分技能接入 DSH。 | **社区扩展** · 迁移配置与调用另一个 Agent 是不同能力；兼容范围见文档。 |
| [DSH-CC](https://github.com/dsh-cc/dsh-cc) | [![GitHub Stars](https://img.shields.io/github/stars/dsh-cc/dsh-cc?style=social)](https://github.com/dsh-cc/dsh-cc/stargazers) | CLI、DSH 插件；依 DSH 环境 | 在 DSH 上组合 Claude Code 风格的 TUI、技能、Hooks 和工作流。 | **社区探索** · 上游明确说明它不是 Claude Code，也不是 Claude Code 包装器。 |
| [DSH Claude Plugin](https://github.com/snowan/dsh-claude-plugin) | [![GitHub Stars](https://img.shields.io/github/stars/snowan/dsh-claude-plugin?style=social)](https://github.com/snowan/dsh-claude-plugin/stargazers) | DSH provider、Agent SDK；Node.js；需 Claude Code 认证 | 把 Claude Code 接成 DSH 的模型路线，同时由 DSH 管理工具执行与会话。 | **社区探索** · 社区早期实现；锁定的 SDK / DSH 版本及兼容性需逐项核对。 |

<a id="cli"></a>

## 适合 Agent 调用的 CLI

直接操作服务、文件和结构化数据，减少对 GUI 的依赖。

| 项目 | Stars | 接口 / 平台 | 适用场景 | 状态与边界 |
| --- | ---: | --- | --- | --- |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | [![GitHub Stars](https://img.shields.io/github/stars/yt-dlp/yt-dlp?style=social)](https://github.com/yt-dlp/yt-dlp/stargazers) | CLI、JSON；音视频站点 | 为有权处理的媒体任务提供下载、元信息提取与批处理入口。 | **基础工具** · 站点适配变化快；按上游更新并确认任务权限。 |
| [MarkItDown](https://github.com/microsoft/markitdown) | [![GitHub Stars](https://img.shields.io/github/stars/microsoft/markitdown?style=social)](https://github.com/microsoft/markitdown/stargazers) | CLI、Python；文档 / 多媒体文件 | 将 PDF、Office 等内容转换为 Markdown，便于 Agent 阅读和分析。 | **基础工具** · 偏内容提取；不保证还原原始排版。 |
| [RTK](https://github.com/rtk-ai/rtk) | [![GitHub Stars](https://img.shields.io/github/stars/rtk-ai/rtk?style=social)](https://github.com/rtk-ai/rtk/stargazers) | CLI、Hooks、代理；macOS / Windows / Linux | 过滤和压缩命令输出，让 Agent 更高效地读取构建、测试与仓库信息。 | 完整版本、OSS 版本和 API 代理的许可及功能有区别。 |
| [FFmpeg / ffprobe](https://github.com/FFmpeg/FFmpeg) | [![GitHub Stars](https://img.shields.io/github/stars/FFmpeg/FFmpeg?style=social)](https://github.com/FFmpeg/FFmpeg/stargazers) | CLI、JSON；音视频文件 | 批量转码、剪辑、抽帧，并通过 ffprobe 检查媒体信息。 | **基础工具** · GitHub 是上游镜像；许可取决于构建所启用组件。 |
| [rclone](https://github.com/rclone/rclone) | [![GitHub Stars](https://img.shields.io/github/stars/rclone/rclone?style=social)](https://github.com/rclone/rclone/stargazers) | CLI、API；云存储 / 本地文件 | 在云盘、对象存储与本地之间复制、同步和校验文件。 | **基础工具** · 适合资料交付和备份流程；同步策略须明确。 |
| [GitHub CLI（gh）](https://github.com/cli/cli) | [![GitHub Stars](https://img.shields.io/github/stars/cli/cli?style=social)](https://github.com/cli/cli/stargazers) | CLI、JSON、API；GitHub | 官方 CLI，用于仓库、Issue、PR、Actions 和 GitHub API 自动化。 | **基础工具** · 比通过网页逐个点击更适合明确的 GitHub 工作流。 |
| [Pandoc](https://github.com/jgm/pandoc) | [![GitHub Stars](https://img.shields.io/github/stars/jgm/pandoc?style=social)](https://github.com/jgm/pandoc/stargazers) | CLI；文档文件 | 在 Markdown、HTML、DOCX 等格式之间转换，制作自动化文档产物。 | **基础工具** · PDF 等输出可能需要额外排版引擎。 |
| [jq](https://github.com/jqlang/jq) | [![GitHub Stars](https://img.shields.io/github/stars/jqlang/jq?style=social)](https://github.com/jqlang/jq/stargazers) | CLI、管道；JSON 数据 | 筛选、转换和汇总结构化输出，连接 Agent 与各类 API / CLI。 | **基础工具** · 适合结果校验与数据整形，本身不含模型。 |
| [Google Workspace CLI（gws）](https://github.com/googleworkspace/cli) | [![GitHub Stars](https://img.shields.io/github/stars/googleworkspace/cli?style=social)](https://github.com/googleworkspace/cli/stargazers) | CLI、JSON、Skills；Google Workspace API | 以结构化命令操作 Drive、Gmail、Calendar、Docs、Sheets 等服务。 | 仓库归属 googleworkspace，但 README 明确写明非官方支持产品。 |
| [gogcli（gog）](https://github.com/openclaw/gogcli) | [![GitHub Stars](https://img.shields.io/github/stars/openclaw/gogcli?style=social)](https://github.com/openclaw/gogcli/stargazers) | CLI、JSON；Google Workspace API | 面向脚本与 Agent 的 Workspace 客户端，支持账号路由与机器可读输出。 | 社区工具；当前规范仓库为 openclaw/gogcli。 |
| [MCPorter](https://github.com/openclaw/mcporter) | [![GitHub Stars](https://img.shields.io/github/stars/openclaw/mcporter?style=social)](https://github.com/openclaw/mcporter/stargazers) | CLI、TypeScript；MCP 工具 | 从命令行发现、调用 MCP 工具，也可将工具封装成独立 CLI。 | 它是 MCP 客户端与桥接层；不是另一个电脑操作驱动。 |
| [Gemini API CLI](https://github.com/google-gemini/gemini-api-cli) | [![GitHub Stars](https://img.shields.io/github/stars/google-gemini/gemini-api-cli?style=social)](https://github.com/google-gemini/gemini-api-cli/stargazers) | CLI、JSON；macOS / Windows / Linux | 让现有 Agent 从 shell 调用 Gemini 模型、多媒体生成、文件分析与托管 Agent。 | **官方实验性** · 无状态 API 客户端；与 Gemini CLI、Antigravity CLI 两种 Harness 区分。 |

<a id="sandbox"></a>

## 虚拟电脑与隔离环境

给自动化任务提供独立桌面、浏览器或文件环境。运行环境本身不等于完整 Agent。

| 项目 | Stars | 接口 / 平台 | 适用场景 | 状态与边界 |
| --- | ---: | --- | --- | --- |
| [Windows in Docker](https://github.com/dockur/windows) | [![GitHub Stars](https://img.shields.io/github/stars/dockur/windows?style=social)](https://github.com/dockur/windows/stargazers) | Docker、Web、RDP；Linux 主机上的 Windows VM | 用容器入口管理 Windows 虚拟机，给桌面自动化准备测试环境。 | 需要虚拟化支持；仓库许可不包含 Windows 客体授权。 |
| [Cua / Lume / Spaces](https://github.com/trycua/cua) | [![GitHub Stars](https://img.shields.io/github/stars/trycua/cua?style=social)](https://github.com/trycua/cua/stargazers) | CLI、SDK、App；依组件；macOS / Linux 等 | 提供 Agent 桌面、虚拟机生命周期、沙箱和电脑操作基础设施。 | Driver、Lume 与 Spaces 的许可不同；按具体组件选择。 |
| [Browserless](https://github.com/browserless/browserless) | [![GitHub Stars](https://img.shields.io/github/stars/browserless/browserless?style=social)](https://github.com/browserless/browserless/stargazers) | WebSocket、HTTP API、Docker；远端浏览器 / 云端 | 托管或自建无头浏览器服务，让 Playwright、Puppeteer 和 Agent 远程连接执行网页任务。 | 远程浏览器会话与本机登录态分离；部署与商业许可见上游。 |
| [Tart](https://github.com/openai/tart) | [![GitHub Stars](https://img.shields.io/github/stars/openai/tart?style=social)](https://github.com/openai/tart/stargazers) | CLI；Apple Silicon；macOS / Linux VM | 构建、运行与管理虚拟机，适合可复现的 Mac 自动化环境。 | 当前仓库已迁至 openai/tart；它提供 VM，不提供任务规划。 |
| [AIO Sandbox](https://github.com/agent-infra/sandbox) | [![GitHub Stars](https://img.shields.io/github/stars/agent-infra/sandbox?style=social)](https://github.com/agent-infra/sandbox/stargazers) | HTTP API、MCP、Docker；Linux 容器 | 把浏览器、终端、文件、VS Code 和 Jupyter 放入一个 Agent 环境。 | 需配置访问认证；容器内服务和宿主权限应按实际任务设置。 |
| [Terminal Mac](https://github.com/govijr/terminal-mac) | [![GitHub Stars](https://img.shields.io/github/stars/govijr/terminal-mac?style=social)](https://github.com/govijr/terminal-mac/stargazers) | CLI、MCP、Skill；Apple Silicon；macOS 14+ | 在终端查看、控制独立 macOS 虚拟机，给电脑操作 Agent 一个隔离桌面。 | **早期候选版** · 客体需首次设置，不继承宿主应用和登录会话；上游仍待干净机器实时验收。 |
| [E2B Desktop Sandbox](https://github.com/e2b-dev/desktop) | [![GitHub Stars](https://img.shields.io/github/stars/e2b-dev/desktop?style=social)](https://github.com/e2b-dev/desktop/stargazers) | Python、JavaScript SDK；Linux 云桌面 | 提供可编程隔离桌面、截图、键鼠和流式查看，用作 Agent 执行环境。 | 此仓库保留模板和示例；Desktop SDK 已迁入 e2b-dev/E2B。 |
| [AI SDK Computer Use Demo](https://github.com/vercel-labs/ai-sdk-computer-use) | [![GitHub Stars](https://img.shields.io/github/stars/vercel-labs/ai-sdk-computer-use?style=social)](https://github.com/vercel-labs/ai-sdk-computer-use/stargazers) | Next.js、AI SDK；Vercel Sandbox | Vercel 官方演示，把模型工具调用、远程桌面与 VNC 展示连成应用。 | **官方示例** · Demo 与 Agent Desktop 不同；需要模型与 Sandbox 服务配置。 |

<a id="remote"></a>

## 远程控制与自动化

从手机指挥 Agent、连接远端主机、持久运行任务到远程桌面接管。具体组合见远程自动化方案。

| 项目 | Stars | 接口 / 平台 | 适用场景 | 状态与边界 |
| --- | ---: | --- | --- | --- |
| [RustDesk](https://github.com/rustdesk/rustdesk) | [![GitHub Stars](https://img.shields.io/github/stars/rustdesk/rustdesk?style=social)](https://github.com/rustdesk/rustdesk/stargazers) | 远程桌面、客户端；多平台 | 远程查看和接管电脑桌面，适合安装、登录、排障与人工接管自动化任务。 | 远程桌面不是 AI 规划器；自动操作仍需 Agent 与执行工具。 |
| [frp](https://github.com/fatedier/frp) | [![GitHub Stars](https://img.shields.io/github/stars/fatedier/frp?style=social)](https://github.com/fatedier/frp/stargazers) | CLI、反向代理；多平台 | 为 NAT 后的 SSH、Web 或其他服务建立转发通路。 | **基础工具** · 是网络连接组件；服务本身仍需身份验证与访问控制。 |
| [Ansible](https://github.com/ansible/ansible) | [![GitHub Stars](https://img.shields.io/github/stars/ansible/ansible?style=social)](https://github.com/ansible/ansible/stargazers) | CLI、YAML、SSH；服务器 / 网络设备 | 将远端安装、配置、部署和巡检固化成可重复的自动化任务。 | **基础工具** · 适合多机器确定性操作；不是 GUI 驱动。 |
| [tmux](https://github.com/tmux/tmux) | [![GitHub Stars](https://img.shields.io/github/stars/tmux/tmux?style=social)](https://github.com/tmux/tmux/stargazers) | CLI、终端会话；Linux / macOS / BSD 等 | 让远端终端会话在断开 SSH 后继续运行，支持重新连接和查看任务输出。 | **基础工具** · 不提供网络或模型服务；常与 SSH 和 Agent CLI 组合。 |
| [Tailscale](https://github.com/tailscale/tailscale) | [![GitHub Stars](https://img.shields.io/github/stars/tailscale/tailscale?style=social)](https://github.com/tailscale/tailscale/stargazers) | CLI、私有网络；多平台 | 连接手机、个人电脑与服务器，为远程 Agent、SSH 和桌面工具提供网络通路。 | **基础工具** · 负责设备连通与访问控制；GUI 控制仍需相应驱动或远程桌面工具。 |
| [Happy](https://github.com/slopus/happy) | [![GitHub Stars](https://img.shields.io/github/stars/slopus/happy?style=social)](https://github.com/slopus/happy/stargazers) | App、Web、CLI、中继；手机 / 桌面 / 运行主机 | 从手机或网页继续 Claude Code、Codex 等会话，查看任务进展并远程交互。 | 原始 CLI 与新桌面 Harness 的能力不同；桌面应用有独立仓库。 |
| [cc-connect](https://github.com/chenhg5/cc-connect) | [![GitHub Stars](https://img.shields.io/github/stars/chenhg5/cc-connect?style=social)](https://github.com/chenhg5/cc-connect/stargazers) | CLI、消息机器人；飞书 / 钉钉 / Telegram 等 | 把本地编码 Agent 接入即时通信渠道，从聊天窗口发任务、查看输出和继续工作。 | 按具体 Agent 与渠道支持表配置；多数渠道无需公网入站端口。 |
| [MeshCentral](https://github.com/Ylianst/MeshCentral) | [![GitHub Stars](https://img.shields.io/github/stars/Ylianst/MeshCentral?style=social)](https://github.com/Ylianst/MeshCentral/stargazers) | Web、设备 Agent；多设备 | 自托管设备管理平台，集中提供远程桌面、终端和文件管理。 | 适合多机器接入与维护；需要部署服务并安装设备端。 |
| [HAPI](https://github.com/tiann/hapi) | [![GitHub Stars](https://img.shields.io/github/stars/tiann/hapi?style=social)](https://github.com/tiann/hapi/stargazers) | CLI、Hub、App、Web；手机 / 桌面 / 运行主机 | 将本机 Agent 会话连接到手机、PWA 和 Telegram Mini App，支持远程接管与审批。 | Web / PWA 与原生客户端的分发和收费方式不同。 |
| [OpenSSH Portable](https://github.com/openssh/openssh-portable) | [![GitHub Stars](https://img.shields.io/github/stars/openssh/openssh-portable?style=social)](https://github.com/openssh/openssh-portable/stargazers) | SSH、SCP、SFTP；Unix / Linux / macOS 等 | 在远端执行 CLI、传输任务文件和建立隧道，是服务器自动化的基础入口。 | **基础工具** · 此仓库为 Portable 实现；Windows 平台安装与版本另看其发行说明。 |
| [Apache Guacamole](https://github.com/apache/guacamole-server) | [![GitHub Stars](https://img.shields.io/github/stars/apache/guacamole-server?style=social)](https://github.com/apache/guacamole-server/stargazers) | Web 网关、RDP、VNC、SSH；浏览器到远程主机 | 通过浏览器访问远端桌面和终端，为远程自动化提供观察与接管入口。 | 该仓库为 guacd 服务端；Web 应用位于 guacamole-client。 |

<a id="mobile"></a>

## 手机与模拟器自动化

覆盖 Android、iOS、真机、模拟器和可复用 UI 测试流程。

| 项目 | Stars | 接口 / 平台 | 适用场景 | 状态与边界 |
| --- | ---: | --- | --- | --- |
| [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) | [![GitHub Stars](https://img.shields.io/github/stars/zai-org/Open-AutoGLM?style=social)](https://github.com/zai-org/Open-AutoGLM/stargazers) | Python、CLI、设备驱动；Android / HarmonyOS / iOS 路径 | 智谱的手机 Agent 模型与框架，通过视觉理解和设备动作完成任务。 | 各平台后端不同；模型权重与框架部署要求分别看上游。 |
| [Appium](https://github.com/appium/appium) | [![GitHub Stars](https://img.shields.io/github/stars/appium/appium?style=social)](https://github.com/appium/appium/stargazers) | WebDriver、SDK；Android / iOS 等 | 跨平台应用自动化底座，可让 Agent 生成或运行可复用的设备操作脚本。 | **基础工具** · 需要安装对应 driver；不是开箱即用的自然语言 Agent。 |
| [Maestro](https://github.com/mobile-dev-inc/Maestro) | [![GitHub Stars](https://img.shields.io/github/stars/mobile-dev-inc/Maestro?style=social)](https://github.com/mobile-dev-inc/Maestro/stargazers) | CLI、YAML、MCP；移动应用 / Web | 用可读流程描述 UI 操作与断言，适合把 Agent 探索结果固化为测试。 | **基础工具** · 支持模拟器及 Android 真机；当前上游说明尚不支持 iOS 真机。 |
| [Mobile MCP](https://github.com/mobile-next/mobile-mcp) | [![GitHub Stars](https://img.shields.io/github/stars/mobile-next/mobile-mcp?style=social)](https://github.com/mobile-next/mobile-mcp/stargazers) | MCP；Android / iOS | 连接真机、模拟器与云设备，通过界面快照或截图驱动移动应用。 | 不同设备路径有不同依赖；不是所有设备都零配置。 |
| [uiautomator2](https://github.com/openatx/uiautomator2) | [![GitHub Stars](https://img.shields.io/github/stars/openatx/uiautomator2?style=social)](https://github.com/openatx/uiautomator2/stargazers) | Python、CLI；Android | 利用 Android UIAutomator 定位元素、操作设备和读取界面层级。 | **基础工具** · 适合 Android 原生 UI 自动化；需要可连接的设备。 |
| [agent-qa](https://github.com/vostride/agent-qa) | [![GitHub Stars](https://img.shields.io/github/stars/vostride/agent-qa?style=social)](https://github.com/vostride/agent-qa/stargazers) | CLI、Dashboard、MCP；Web、Android、iOS | 通过自然语言测试网页、Android 与 iOS，结合 memidex 持久记忆、自我改进及逐步截图证据。 | [官网](https://vostride.com)；FSL-1.1-ALv2。模型 API 与设备环境需自行配置；记忆以可审阅文件保存，自我改进会验证运行经验。 |
| [Terminal Phone](https://github.com/govijr/terminal-phone) | [![GitHub Stars](https://img.shields.io/github/stars/govijr/terminal-phone?style=social)](https://github.com/govijr/terminal-phone/stargazers) | CLI、MCP；Apple Silicon Mac；iOS | 在终端展示 iOS 模拟器或已配对 iPhone，让人和 Agent 共用设备操作接口。 | **早期项目** · 需要 Xcode；真机控制另有配对和授权要求。 |

<a id="workflow"></a>

## 工作流与持续自动化

把单次任务连接到 CI、事件、调度、重试和结果交付。

| 项目 | Stars | 接口 / 平台 | 适用场景 | 状态与边界 |
| --- | ---: | --- | --- | --- |
| [n8n](https://github.com/n8n-io/n8n) | [![GitHub Stars](https://img.shields.io/github/stars/n8n-io/n8n?style=social)](https://github.com/n8n-io/n8n/stargazers) | Web UI、API、工作流；自托管 / 云端 | 通过连接器、代码节点和 AI 节点编排跨服务业务自动化。 | 源码可见、fair-code；不要直接标为 OSI 开源软件。 |
| [Prefect](https://github.com/PrefectHQ/prefect) | [![GitHub Stars](https://img.shields.io/github/stars/PrefectHQ/prefect?style=social)](https://github.com/PrefectHQ/prefect/stargazers) | Python、CLI、API；Python 工作流 | 为批处理和 Agent 周边流程提供调度、重试、状态与可观测性。 | **基础工具** · 负责执行编排；电脑操作仍需另接工具。 |
| [Windmill](https://github.com/windmill-labs/windmill) | [![GitHub Stars](https://img.shields.io/github/stars/windmill-labs/windmill?style=social)](https://github.com/windmill-labs/windmill/stargazers) | CLI、API、脚本；自托管 / 云端 | 把 Python、TypeScript、Bash 等脚本发布为任务、API 和可编排工作流。 | 社区发行二进制、源码构建和企业功能的许可有区别。 |
| [Claude Code Action](https://github.com/anthropics/claude-code-action) | [![GitHub Stars](https://img.shields.io/github/stars/anthropics/claude-code-action?style=social)](https://github.com/anthropics/claude-code-action/stargazers) | GitHub Actions；CI | 让 Claude Code 处理 Issue、PR 问答、代码变更和审查任务。 | 按事件设置触发范围与工具权限。 |
| [GitHub Agentic Workflows](https://github.com/github/gh-aw) | [![GitHub Stars](https://img.shields.io/github/stars/github/gh-aw?style=social)](https://github.com/github/gh-aw/stargazers) | gh 扩展、Markdown、Actions；GitHub Actions | 把带 YAML 配置的 Markdown 任务编译成 Agent 工作流，执行仓库维护与分析。 | 模型执行、确定性 CI 和写入结果各有不同职责。 |
| [Codex GitHub Action](https://github.com/openai/codex-action) | [![GitHub Stars](https://img.shields.io/github/stars/openai/codex-action?style=social)](https://github.com/openai/codex-action/stargazers) | GitHub Actions；CI | 将 Codex 任务接入 PR、Issue 或代码流水线。 | Action 需要配置模型认证及工作流权限；不是桌面定时任务。 |

<a id="scripting"></a>

## 系统脚本与传统自动化

让 Agent 调用已有的确定性脚本和系统能力。

| 项目 | Stars | 接口 / 平台 | 适用场景 | 状态与边界 |
| --- | ---: | --- | --- | --- |
| [Hammerspoon](https://github.com/Hammerspoon/hammerspoon) | [![GitHub Stars](https://img.shields.io/github/stars/Hammerspoon/hammerspoon?style=social)](https://github.com/Hammerspoon/hammerspoon/stargazers) | Lua、控制接口；macOS | 用 Lua 组合窗口、快捷键、应用与系统事件，构建可复用 Mac 自动化。 | **基础工具** · 适合明确的本地操作，不包含自然语言规划器。 |
| [AutoHotkey](https://github.com/AutoHotkey/AutoHotkey) | [![GitHub Stars](https://img.shields.io/github/stars/AutoHotkey/AutoHotkey?style=social)](https://github.com/AutoHotkey/AutoHotkey/stargazers) | 脚本、CLI；Windows | 将键鼠、窗口与热键操作编写成脚本，作为 Agent 的确定性执行工具。 | **基础工具** · 应区分 v1 与 v2 语法。 |
| [PyAutoGUI](https://github.com/asweigart/pyautogui) | [![GitHub Stars](https://img.shields.io/github/stars/asweigart/pyautogui?style=social)](https://github.com/asweigart/pyautogui/stargazers) | Python；macOS / Windows / Linux | 提供键鼠、截图和基础图像定位，用于自建 GUI 自动化工具。 | **基础工具** · 坐标与屏幕状态相关；运行环境支持须实际验证。 |

<a id="benchmark"></a>

## 评测与研究环境

用真实任务与可重复评测判断能力；不把演示视频或不同协议的分数当作统一排名。

| 项目 | Stars | 接口 / 平台 | 适用场景 | 状态与边界 |
| --- | ---: | --- | --- | --- |
| [OSWorld](https://github.com/xlang-ai/OSWorld) | [![GitHub Stars](https://img.shields.io/github/stars/xlang-ai/OSWorld?style=social)](https://github.com/xlang-ai/OSWorld/stargazers) | 评测环境、Python；真实桌面环境 | 评估多模态 Agent 在真实电脑任务中的完成情况。 | **评测** · 研究基准；报告成绩时需注明版本、模型、步数及评分协议。 |
| [BrowserGym](https://github.com/ServiceNow/BrowserGym) | [![GitHub Stars](https://img.shields.io/github/stars/ServiceNow/BrowserGym?style=social)](https://github.com/ServiceNow/BrowserGym/stargazers) | Python、Gym；浏览器任务 | 为浏览器 Agent 提供统一任务环境与评测接口。 | **评测** · 用于研发和可重复评估，不是日常自动化产品。 |

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

动态徽章的数值由 Shields.io 自动更新。`update_stars.py` 使用已登录的 GitHub CLI 更新分类排序参考数据；获取失败时保留旧数据。详细规则见 [CONTRIBUTING.md](CONTRIBUTING.md)。本项目不按 Star 数自动收录，也不把未经实测的条目标为实测推荐。

相关清单：[Awesome MCP ZH](https://github.com/yzfly/Awesome-MCP-ZH) · [Awesome DSH Skills](https://github.com/yzfly/awesome-dsh-skills)。

## 许可

本仓库的原创整理内容和维护脚本使用 [MIT License](LICENSE)。被收录项目、商标、模型和服务遵循各自上游条款。
