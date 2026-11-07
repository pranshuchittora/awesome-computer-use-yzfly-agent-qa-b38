# 贡献指南

欢迎推荐项目、纠正描述、更新迁移地址和报告失效链接。请保持清单适合中文读者快速选型。

## 收录标准

1. 优先使用原作者或官方组织的 GitHub 仓库，避免镜像、搬运、同名误认。
2. 项目应有明确的自动化用途、README / 文档，以及安装、示例或可运行入口。
3. 说明它属于产品、执行工具、Agent、运行环境、示例还是评测。CLI 不必内置 AI，但应能直接帮助 Agent 完成任务。
4. 写出具体平台与接口。不要把“支持 MCP”推断成所有客户端、模型或操作系统都已支持。
5. 对实验性、小型新项目、归档项目及重要限制如实标注。避免“最好”“最快”或未经同条件验证的比较。
6. 公开仓库不自动等于开源产品。记录上游许可，区分源码、二进制、模型权重和商业服务。
7. 补充至少一个直接支持描述的上游来源，并更新核验日期。文档核验不能写成实际安装测试。

## 修改流程

项目条目的唯一数据源是 `data/projects.json`，`README.md` 由脚本生成。新条目使用已有字段：

| 字段 | 内容 |
| --- | --- |
| `name` | 展示名称 |
| `category` | `desktop`、`browser`、`harness`、`dsh`、`cli`、`sandbox`、`mobile`、`workflow`、`scripting`、`benchmark` |
| `repository` | 当前规范仓库 `owner/repo` |
| `github` | 仓库或明确组件的 GitHub 链接 |
| `interfaces` | CLI、MCP、SDK 等接口数组 |
| `platforms` | 实际支持的平台或执行环境 |
| `description` | 一句话说明它能做什么，以及适用任务 |
| `note` | 关键限制、依赖或需要区分的能力 |
| `status` | 项目、官方组件、官方示例、社区扩展、社区探索、实验性、基础工具或评测等准确说明 |
| `license` | 从上游确认的许可或范围说明；不确定就写明 |
| `sources` | 支持描述的上游文档 URL 数组 |
| `checked_at` | 本次核验日期，`YYYY-MM-DD` |
| `verification` | 当前使用 `upstream-docs`；增加实测等级前先定义可复核证据要求 |

同一仓库的不同组件仅在用途和链接均明确不同的情况下分开列出，不用重复条目填充数量。迁移时更新规范地址与来源，不保留一组新旧重复条目。

```bash
python3 scripts/render_readme.py
python3 scripts/render_readme.py --check
git diff --check
```

渲染器只用 Python 标准库，检查字段、重复链接、分类和 README 一致性，不联网、不执行收录工具。提交前还需手动打开新增链接核对内容。

选型建议和阅读资料分别维护在 `docs/guide.md`、`docs/reading.md`。调整 README 的导言或表格结构时修改 `scripts/render_readme.py`。

请在 PR 里说明真实使用场景和上游证据。只建议项目也可以使用 Issue 模板。
