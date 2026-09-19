# v1.0 与当前版技能/Provider 对比研究

> 研究日期：2026-09-19
> 比较基线：`origin/v1.0` / `25312e89dc71ef05b1fb9b96d256da6a8e5429f7`
> 当前工作树：`main` / `f901148cdd5211ce74874fdc185bb81eff58c41f`
> 范围：A1-A15 的技能引用、provider 适配性与推荐映射。本文只做研究，不修改现有流程。

## 结论摘要

这次变化不是简单地“把 Superpowers、UI/UX 技能删掉”，而是把两种不同层次的概念替换了：

- v1.0 写的是**具体 provider 和命令**，例如 gstack `/office-hours`、`/design-consultation`，Superpowers `writing-plans`、`test-driven-development`，以及 OpenSpec `/openspec:propose`。
- 当前版写的是**能力合同（capability IDs）**，例如 `product.discovery`、`design.system`、`development.tdd`。它们不是可安装、可直接调用的技能，而是“这一步必须得到什么结果”的接口名；运行时仍应解析到具体 provider。

因此，不能笼统判断“旧技能还是新技能更好”：

1. **作为仓库架构，当前的 capability 层更合理。** 它避免绑定单一宿主、过时命令和未安装的 agent，也让缺少插件时仍可使用仓库原生命令完成结果。
2. **作为开箱即用的执行指引，v1.0 更具体。** 当前映射没有为多数步骤给出经过验证的首选 provider，实际执行者容易退化成“主 agent 自己做”，从而丢掉 Superpowers 的纪律、gstack 的产品/设计/浏览器闭环和 OpenSpec 的制品治理。
3. **最佳方案是两层并存，而不是回滚。** 保留 capability ID 作为稳定合同；在 adapter 中增加“按场景推荐、发现后调用”的 provider profile，并记录验证日期、宿主、命令别名、是否会写文件或产生外部副作用。
4. **Superpowers 应恢复为 A1、A6、A9、A10、A12 的推荐 provider，而非硬依赖。** 它最强的是从设计、计划、TDD 到独立审查、完成前验证的工程纪律；不擅长 UI 设计、部署和生产观测。
5. **gstack 的 UI/UX 技能应恢复为 A2-A3 的推荐 provider。** 其中 greenfield 用 `design-consultation`，实施前设计审查用 `plan-design-review`，已有站点的视觉审查/修复才用 `design-review`。v1.0 把 `design-review` 用在“实施前 demo sign-off”上并不精确。
6. **OpenSpec 最适合 A1/A6/A7/A9 的变更制品生命周期，不应被描述成专门的 API 文档工具。** 当前官方工作流是 `explore → propose → apply → sync → archive`，命令已从 v1.0 的 `/openspec:*` 演进为 `/opsx:*`；这正说明 capability 抽象是必要的。
7. **当前文档把 gstack、Superpowers、OpenSpec 一概称为 “Claude Code Legacy” 已经过时。** 截至研究日，gstack 官方安装器列出 Codex host，Superpowers 官方 README 列出 Codex App/CLI 插件，OpenSpec 也支持多种 AI 工具。它们是“可选第三方 provider”，但不应统称为 Claude legacy。
8. **用户记忆中的 UI UX Pro Max 并不在本仓库 v1.0 或后续提交中。** 它是一个真实、当前支持 Codex 的外部设计技能，适合补充 `design.system`，但不能当作“被本次提交删掉的历史引用”。
9. **当前仍有两个 capability 设计缺口。** A12 缺少明确的 `verification.completion`（或等价）合同，因而没有直接承接 Superpowers `verification-before-completion`；`delivery.release` 又同时覆盖 A8 环境、A11 PR/CI、A13 部署/恢复，范围过宽且混合不同副作用。

总体判断：**迁移方向合理，provider 落地不足。** A7、A8、A11-A14 的替换明显提升了安全性和适用性；A1、A2、A3、A6、A9、A10、A12、A15 则需要把优秀的具体 provider 重新补回推荐层。

## 一、v1.0 的定位与改动时间线

### 1.1 “上一次 v1.0”是哪个版本

Git 证据是确定的：

```text
origin/v1.0 -> 25312e8 feat: initial release — full-stack development lifecycle skill
origin/main -> f901148 feat: define 15-step lifecycle workflow
local main  -> f901148 feat: define 15-step lifecycle workflow
```

复现命令：

```bash
git branch -avv
git log --reverse --format='%H %ad %s' --date=iso-strict
git show origin/v1.0:SKILL.md
git show origin/v1.0:references/skills-mapping.md
```

v1.0 的 15 步具体调用可见 [历史 SKILL.md](https://github.com/icestarx/full-stack-skill/blob/25312e89dc71ef05b1fb9b96d256da6a8e5429f7/SKILL.md#L76-L325)，三套生态的逐步比较可见 [历史 skills-mapping.md](https://github.com/icestarx/full-stack-skill/blob/25312e89dc71ef05b1fb9b96d256da6a8e5429f7/references/skills-mapping.md)。

用户记忆中的“uiux”不是一个名为 `uiux` 的独立技能。v1.0 实际引用的是 gstack 的 UI/UX 组合：

- `/design-consultation`
- `/plan-design-review`
- `/design-html`
- `/design-review`
- Claude artifacts（原型载体，而非仓库内定义的 skill）

### 1.2 具体技能何时被换掉

首次、也是最大规模的替换发生在提交：

```text
aeee990abc95fcc11c372bdb30561fa39c56d51f
feat: add portable Codex runtime adapter
```

该提交：

- 新增 `references/platform-adapters.md`；
- 将 `references/skills-mapping.md` 从具体命令表改为 capability 映射；
- 将 gstack、Superpowers、OpenSpec 和固定 reviewer agents 从 required dependencies 改成 optional providers；
- 把 `setup` 从仅检查 `~/.claude/*` 改为检查核心仓库结构、宿主和可选 provider；
- 明确“未发现 provider 前不要输出其命令；provider 缺失时使用 main agent + repository-native tools”。

后续提交没有重新引入新的具体 provider，而是在这一抽象上继续完善：

| 提交 | 主要变化 | 对技能映射的影响 |
|---|---|---|
| `50d6dac` | 强化需求和 traceability | 新增 `product.requirements-review`，更强调证据链 |
| `4a309e0` | 采用 four-track 模型 | 从步骤中心进一步转向轨道、门禁与垂直切片 |
| `6c34729` | 长期交付加固 | 收缩固定模板/硬规则，引入风险触发和 eval |
| `f901148` | 恢复 A1-A15 默认主路线 | 保留 capability 映射，同时重新把 15 步作为主叙事 |

迁移意图可从当前 [platform-adapters.md](../references/platform-adapters.md) 和 [DEPENDENCIES.md](../DEPENDENCIES.md) 直接读出，但提交说明本身没有解释“为什么每个旧 provider 被换掉”。下文对合理性的判断属于基于 diff、宿主兼容性和 provider 官方合同的分析，而不是提交作者留下的逐项决策记录。

## 二、评估方法：能力和技能不能混为一谈

本文用四层模型评价每一步：

1. **Outcome / capability**：必须完成的结果，例如“有可审查的 UX 状态覆盖”。
2. **Provider**：实现该结果的技能包或工作流，例如 gstack、Superpowers、OpenSpec。
3. **Project-native tool**：项目自身的测试、CI、迁移、部署和可观测性工具，通常是最可靠的确定性证据。
4. **Fallback**：没有 specialist 时由 main agent 按仓库模板和原生命令完成。

当前版的 `product.discovery`、`design.system` 等属于第 1 层，不是第 2 层。因此，“当前能力名比 Superpowers 好不好用”不是有效比较；有效问题是：**该 capability 是否定义正确，以及运行时选到哪个 provider 最合适。**

这种分层也符合 Codex 官方技能机制：Codex 先根据 skill 的 `name` 和 `description` 做显式或隐式选择，选中后才加载完整 `SKILL.md`；仓库技能、用户技能和系统技能可以来自不同位置。官方也建议一个 skill 聚焦一个任务，并明确输入输出。[OpenAI 官方：构建技能](https://developers.openai.com/zh-Hans/docs/build-skills#chatgpt-%E5%92%8C-codex-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E6%8A%80%E8%83%BD)

## 三、Provider 全面比较

### 3.1 Superpowers

官方定位是“软件开发方法论 + 可组合技能”。当前官方技能库仍包含 `brainstorming`、`writing-plans`、`subagent-driven-development`、`test-driven-development`、`requesting-code-review`、`receiving-code-review` 和 `verification-before-completion`，并提供 Codex App/CLI 的官方插件安装方式。[Superpowers README](https://github.com/obra/superpowers/blob/5bf4e78011075bcfc0dc295f0724994cd123ee71/README.md)

优势：

- 设计批准 → 实施计划 → 执行 → 独立审查 → 完成前验证的纪律完整。
- TDD 合同非常具体：必须看到正确的失败，再写最小实现，再跑全套测试。[TDD skill](https://github.com/obra/superpowers/blob/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/test-driven-development/SKILL.md)
- `subagent-driven-development` 包含 spec compliance 和 code quality 两段审查，适合稳定计划下的多任务执行。[Subagent-driven development](https://github.com/obra/superpowers/blob/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/subagent-driven-development/SKILL.md)
- `verification-before-completion` 明确要求“证据先于完成声明”，非常适合 A12 和所有 gate。[Verification before completion](https://github.com/obra/superpowers/blob/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/verification-before-completion/SKILL.md)

局限：

- 不是产品运营、完整 UI 设计、部署或生产监控套件。
- 当前 `brainstorming` 有严格的人类批准 gate，并把任务分为 spike/bounded/architectural；若 A1-A3 已由本仓库完成，再无条件调用会重复提问和重复建文档。[Brainstorming skill](https://github.com/obra/superpowers/blob/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/brainstorming/SKILL.md)
- “任何功能都严格 TDD”对生成代码、纯配置、视觉探索和遗留系统 characterization 需要按其例外机制处理，不能把方法论口号替代风险判断。
- subagent 工作流有额外 token、时间和协调成本，小变更不应强制使用。

结论：**A6/A9/A10/A12 的首选工程纪律 provider；A1 的条件 provider。** 从核心依赖降为可选是合理的，但从推荐映射中几乎消失不合理。

### 3.2 gstack（包括用户记忆中的 UI/UX）

gstack 官方把自身定义为贯穿 Think → Plan → Build → Review → Test → Ship → Reflect 的交付系统。当前技能说明覆盖产品发现、CEO/工程/设计计划审查、设计系统、浏览器 QA、PR、部署、canary 和 retro。[gstack README](https://github.com/garrytan/gstack/blob/a6b3a57512ca6d5c6aa5b68f74f736195021f96e/README.md)；[skill deep dives](https://github.com/garrytan/gstack/blob/a6b3a57512ca6d5c6aa5b68f74f736195021f96e/docs/skills.md)

截至研究日，官方 README 已列出 OpenAI Codex CLI 的 `--host codex` 安装路径，因此当前文档中的“Claude Code Legacy Adapter”称呼不再准确。[gstack 多宿主安装表](https://github.com/garrytan/gstack/blob/a6b3a57512ca6d5c6aa5b68f74f736195021f96e/README.md#L103-L130)

优势：

- 三套 provider 中对产品发现、UI/UX、真实浏览器 QA、发布和复盘覆盖最完整。
- `office-hours` 用 forcing questions 挖掘真实需求和最窄切入口；`plan-ceo-review` 单独校准产品范围。
- UI/UX 分工明确：`design-consultation` 建 greenfield design system；`plan-design-review` 审实施前计划；`design-review` 审并修复已运行页面；`design-html` 把批准设计实现为其 Pretext-native HTML/CSS。
- `qa` 能执行测试—修复—复验，`qa-only` 则保持报告只读；这一区分比泛化的 `qa.browser` 更有操作性。
- `ship`、`land-and-deploy`、`canary`、`retro` 形成连续链条。

局限：

- 套件较重，包含 Bun、浏览器、宿主生成和自身状态/遥测机制；不是每个仓库都应安装。
- 多个技能会修改代码、提交、推送、合并或部署。仅凭“进入某一步”不能推定用户授权了外部写操作。
- `qa`/`qa-only` 面向 Web 应用，不是后端 integration-test runner；v1.0 把 `/qa Quick` 描述成“真实数据库集成测试”过度延伸了其合同。
- `setup-deploy` 官方合同是探测部署平台并为 `land-and-deploy` 写配置，不等同于通用的本地环境、数据库、完整 CI/CD 和 staging 建设。
- `design-html` 当前明确是 Pretext-native HTML/CSS 实现，不能作为所有 React/Vue/native app 的通用“生产前端生成器”。
- 高频交互、持久化状态和 opinionated 流程会给小改动带来额外摩擦。

结论：**A1-A3 和 A11-A15 的高价值可选 provider，尤其 UI/UX 仍值得保留；但必须按场景拆分技能并标记副作用。**

### 3.3 OpenSpec

OpenSpec 官方把 `specs/` 定义为当前事实，把 `changes/` 定义为拟议变更；当前默认流程是 `/opsx:explore → /opsx:propose → /opsx:apply → /opsx:sync → /opsx:archive`。`propose` 会生成 proposal、specs、design、tasks，而不只是 API 文档。[OpenSpec overview](https://github.com/Fission-AI/OpenSpec/blob/bae58cf61479986431bb798acbe5a688a591c18c/docs/overview.md)；[workflow](https://github.com/Fission-AI/OpenSpec/blob/bae58cf61479986431bb798acbe5a688a591c18c/docs/workflows.md)；[propose skill](https://github.com/Fission-AI/OpenSpec/blob/bae58cf61479986431bb798acbe5a688a591c18c/skills/openspec-propose/SKILL.md)

优势：

- 对需求/规范 baseline 与 change delta 的生命周期治理最强。
- CLI 提供 scaffold、status、instructions、validate、archive 等确定性操作，适合长期维护和 CI 检查。[CLI reference](https://github.com/Fission-AI/OpenSpec/blob/bae58cf61479986431bb798acbe5a688a591c18c/docs/cli.md)
- `apply` 与 planning artifacts 相连，实施发现变化时可以更新制品，而非让计划与代码永久漂移。
- 多宿主、生成式 skill/command 适配比 v1.0 假定的单一 `/openspec:*` 名称更成熟。

局限：

- 引入新的仓库目录、规范格式和 archive 习惯；已有 ADR、RFC、OpenAPI、issue/PR 体系完善时可能重复。
- 它不替代 UI/UX 设计、代码质量方法、浏览器 QA、部署和生产监控。
- `propose` 产生完整 change artifacts；仅为一个 API schema 强制初始化 OpenSpec 往往过重。
- v1.0 使用的 `/openspec:propose`、`/openspec:apply` 是旧命令体系，当前官方主路径是 `/opsx:*`。固定命令必然产生版本漂移。

结论：**适合已有 OpenSpec 或需要版本化 change/spec delta 的 A1/A6/A7/A9；不是 A7 的默认 API 设计器。** 当前把它抽象成 `spec.change` 很合理，但应保留 provider profile。

### 3.4 UI UX Pro Max 与 Impeccable：不是 v1.0 被替换项，但值得作为当前候选

对全部 Git 历史执行以下检索，没有找到 `ui-ux-pro-max`、`UI UX Pro Max` 或同名 invocation：

```bash
git log --all -S 'ui-ux-pro-max' -- '*.md'
git grep -inE 'ui.?ux.pro.max|ui-ux-pro-max' $(git rev-list --all) -- '*.md'
```

因此，“以前有 uiux 技能”不能归因于本仓库 v1.0。v1.0 中的 UI/UX 实际来自 gstack 设计技能组合。UI UX Pro Max 可能是用户在同一宿主中安装或见过的另一个技能。

UI UX Pro Max 官方仓库目前提供大量 style、palette、font pairing、chart、stack 和 UX guideline 数据，并通过 Python 标准库离线检索为 Web、mobile、desktop 等多栈给出设计系统与实现建议；其安装元数据包含 Codex。[UI UX Pro Max 官方仓库](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)；[v2.15.0 release](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/releases/tag/v2.15.0)

- **强项**：A2 的跨平台设计知识、design-system 规则、技术栈特定建议；离线检索比让模型凭记忆挑字体/颜色更可重复。
- **弱项**：不像 gstack 那样覆盖产品研究 → 多方案 → 人类选择 → 浏览器复核闭环，也不能单独证明 A3 验收或 A12 真实页面质量。
- **推荐**：映射 `design.system`；作为 gstack `design-consultation` 的跨平台替代或补充，不作为 `design.review`/`qa.browser` 的唯一 provider。

Impeccable 也不是 v1.0 provider，但当前提供 1 个核心 skill、多个设计命令和确定性 detector rules，围绕 `PRODUCT.md`/`DESIGN.md` 支持 shape、critique、audit、polish、harden、adapt 等 UI 工作。[Impeccable 官方仓库](https://github.com/pbakaus/impeccable)；[Skill 4.3.1 release](https://github.com/pbakaus/impeccable/releases/tag/skill-v4.3.1)

- **强项**：更适合 A3/A12 的设计批评、deterministic audit 和修复证据。
- **弱项**：不负责产品范围、后端、PR、部署、生产监控；engine/hooks 带来安装与供应链考量。
- **推荐**：UI UX Pro Max 偏 A2 知识/系统，Impeccable 偏 A3/A12 审查，gstack 偏完整产品设计与浏览器交付流程，三者是互补而非简单替代。

### 3.5 当前会话可发现的 Codex provider 候选

研究时的 Codex skill catalog 中已经存在一批可以承接当前 capability 的 provider，但它们属于**本次运行环境**，不能未经发现就写成仓库硬依赖：

| A 步骤 | 当前可发现候选 | 适合的 capability / 边界 |
|---|---|---|
| A1 | `prd-writer` | 新建、审查和增量更新 PRD，可承接 `product.requirements-review`；不自动等同于市场/用户 discovery |
| A2-A3 | `product-design:ideate`、`product-design:audit`、`prototype`、Figma 系列 skills | ideate 做视觉方案，audit 做基于截图的 UX/accessibility 审查，prototype 做低成本状态模型，Figma 做设计上下文/产物；需按任务选择，不能全部调用 |
| A4-A5 | `codebase-design`、`domain-modeling`、`research` | 模块接口/边界、领域术语/ADR、一手资料研究；技术决策仍需 repo evidence |
| A9 | `tdd`、`diagnosing-bugs`、`playwright` | TDD、根因诊断、真实浏览器验证；bug 模式不应直接套 feature implementation 流程 |
| A10 | `code-review`、`security-best-practices`、`security-threat-model` | 通用双轴审查和明确触发的安全专项；安全技能按用户请求/风险和语言支持触发 |
| A12 | `playwright`、`product-design:audit`、security review skills | 产生浏览器/UX/安全专项证据；仍必须由项目原生命令给出 build/test/typecheck 证据 |
| A14 | `sentry` | 读取 Sentry issue/event 和健康数据；只覆盖已连接的错误/事件源，不代表全部 observability |

这张表恰好说明 capability 架构的价值：不同 Codex 安装的 catalog 会变化，核心流程只应声明 outcome；但 adapter 应展示“当前已发现 provider → capability”的解析结果，而不是默默退回 main agent。

### 3.6 v1.0 的 named agents

v1.0 还把 `architect`、`database-reviewer`、`e2e-runner`、`a11y-architect`、`performance-optimizer`、各语言 reviewer 等写成 `~/.claude/agents/` 下的 required agents，却没有记录来源仓库、版本、校验和或 agent contract。

这些名字与 Everything Claude Code（现 ECC）的 agent 集高度吻合；ECC 官方仓库目前列出了 architect、database-reviewer、e2e-runner 和大量语言 reviewer。[ECC README](https://github.com/affaan-m/ECC/blob/main/README.md)；[agent map](https://github.com/affaan-m/ECC/blob/main/docs/COMMAND-AGENT-MAP.md)。但这是名称与目录结构上的推断，不能证明 v1.0 当时引用的就是某个确定的 ECC 版本。

优势：角色窄、上下文隔离，适合高风险专项审查。局限是来源不明导致不可复现，部分 specialist 又具有技术栈偏置（例如数据库 reviewer 可能面向 PostgreSQL/Supabase），并且“agent 名相同”不代表合同相同。

结论：**从 required agents 改为风险触发的 capability 是正确修复。** 若重新提供具体映射，应写完整 provider/source/version，而不是只写 `architect agent`。

### 3.7 Repository-native tools 与主 agent fallback

优势：与真实项目最匹配，测试/构建/迁移/CI 输出是确定性证据，不依赖额外安装。局限：没有 specialist 时，产品、设计、独立审查和复盘质量高度依赖主 agent 自身，且“同一上下文自审”不等于独立评审。

结论：**原生命令应始终优先承担证据生成；fallback 只能保证流程可运行，不能宣称与 specialist 等价。** 当前文档的“provider absence is not a blocker”应补充质量降级和未收集证据，而当前 `Degraded Operation` 已朝这一方向处理。

### 3.8 浏览器、性能和文档检索工具

- Playwright MCP 官方说明指出：coding agent 的多数场景更适合 CLI + skills，因为 token 开销更低；MCP 更适合需要 persistent state 和 rich introspection 的长时间探索循环。[Playwright MCP：MCP vs CLI](https://github.com/microsoft/playwright-mcp#playwright-mcp-vs-playwright-cli) 因而当前 `qa.browser` 抽象优于 v1.0 的固定 MCP/agent 假设，provider 可按任务在 Playwright CLI、skill 和 MCP 间选择。
- Chrome DevTools MCP 擅长 performance trace、network/console 调试和截图，但只覆盖 Chrome 系列浏览器，也带浏览器数据可见性和 telemetry/CrUX 注意事项。[Chrome DevTools MCP key features](https://github.com/ChromeDevTools/chrome-devtools-mcp#key-features) 它适合 `review.performance`/debug supplement，不应成为 A12 的默认唯一审计器。
- Context7 提供当前版本文档检索，但官方 disclaimer 明确其索引为社区贡献，不能保证准确、完整或安全，且 backend/crawler 不开源。[Context7 disclaimer](https://github.com/upstash/context7#disclaimer) 它适合 A4/A7/A9 的资料发现，最终决策仍应由库的官方文档/源码与项目测试验证。

## 四、A1-A15 逐步对比

下表中的“当前”来自 [skills-mapping.md](../references/skills-mapping.md)；“v1.0”来自历史 `SKILL.md` 与 `references/skills-mapping.md`。

| 步骤 | v1.0 provider | 当前 capability / fallback | 对比与优势 | 更换是否合理 | 推荐映射 |
|---|---|---|---|---|---|
| **A1 需求与范围** | gstack `office-hours` + Superpowers `brainstorming`；`plan-ceo-review`；OpenSpec propose 备选 | `product.discovery`、`product.requirements-review`；条件 `product.scope-review`；main-agent requirements workflow | 旧版有真实的 discovery 和批准流程；新版增加了“需求审查”这一旧版缺口，并可处理既有产品 delta | **方向合理，具体性损失较大** | 模糊新产品：`office-hours`；工程设计/批准：Superpowers `brainstorming`；正式 PRD：发现到的 PRD skill；版本化 change：OpenSpec `explore/propose`；范围争议：`plan-ceo-review`。不要默认串行全跑 |
| **A2 UX 合同** | gstack `design-consultation` + `plan-design-review`；按需 `design-html` | `design.system`；条件 `design.prototype`；直接写 UI spec fallback | 新版 outcome 更可移植，也允许非 UI 为 N/A；旧版对设计系统与状态覆盖更可执行 | **抽象合理，但应恢复首选 provider** | Greenfield：`design-consultation`；已有设计系统：直接使用项目 tokens/components；方向探索用设计 ideation/Figma；实施前用 `plan-design-review`；原型用 `design.prototype`。`design-html` 只在其输出技术匹配时使用 |
| **A3 产品确认** | gstack `design-review` + Claude artifacts；冲突时 Superpowers brainstorming | `product.scope-review`、`design.review`；条件 `design.prototype`；结构化人类决策 | 新版把“决策”和“演示载体”分开更正确。当前 gstack `design-review` 是 live-site audit/fix，而不是纯粹的 plan sign-off | **更换合理，并修复了旧映射语义错误** | 可点击/可运行原型 + 人类 decision record；实施前审查优先 `plan-design-review`，已有站点视觉验收才用 `design-review`；范围改变时才回到 `plan-ceo-review`/A1 |
| **A4 勘察与技术决策** | gstack `plan-eng-review` + named `architect`；Superpowers brainstorming | `architecture.review`；条件技术/领域 specialist；repo inspection | 新版先读代码/历史/合同，避免脱离仓库的“大架构设计”；旧版 `plan-eng-review` 的数据流、边界、测试矩阵仍有价值 | **合理** | repo reconnaissance 为必选；已有 plan 且决策较大时用 `plan-eng-review`；架构 specialist 只处理 hard-to-reverse 决策；Superpowers brainstorming 不应在 A1-A3 已批准后无条件重跑 |
| **A5 边界与依赖** | named `architect`；OpenSpec propose 补充 | `architecture.review`；main-agent dependency analysis | 新版避免把 OpenSpec 误当 DDD/模块分解器；也不假设有叫 architect 的 agent | **合理** | 代码调用图、consumer、ownership 和 contract inspection 为核心；domain-modeling/codebase-design/architect specialist 按需；OpenSpec 仅记录已经决定的 spec/module delta |
| **A6 垂直切片计划** | Superpowers `writing-plans`；OpenSpec propose 备选 | `planning.decompose`；main-agent plan/template fallback | capability 正确且允许 slice，不再强制 2-5 分钟粒度；但失去 Superpowers 的文件路径、命令、预期输出级计划质量 | **方向合理，provider 推荐不足** | 稳定且多步骤：Superpowers `writing-plans`；已有 OpenSpec：使用其 `tasks.md`；小变更：change-work-item 直接拆分；计划必须按垂直价值/风险切片，不机械按层拆分 |
| **A7 数据与接口合同** | DB：architect + database-reviewer；API：OpenSpec propose；Superpowers plan 备选 | `architecture.review`；条件 `database.review`、`spec.change`；schema/API inspection + native contract tests | 新版把 DB 和 versioned spec 变为风险触发，增加兼容、version skew、恢复与 contract tests；比“每模块都写 DB+API 文档”更适合真实仓库 | **明显合理** | 权威 schema/OpenAPI/IDL 优先；数据库变更才用 DB specialist；跨版本/长期规范才用 OpenSpec；OpenSpec 管变更生命周期，不替代 OpenAPI/GraphQL schema 本身 |
| **A8 环境与交付就绪** | gstack `setup-deploy` + database-reviewer | `delivery.release` + repo-native environment/build/CI/smoke | v1.0 高估了 `setup-deploy` 范围，并默认所有项目都有 staging/DB；新版按 slice 和风险准备最小可复现环境 | **明显合理** | Docker/devcontainer/IaC/CI/项目脚本优先；若使用 gstack 发布链，再用 `setup-deploy` 配置；只有迁移/数据风险才加 DB review |
| **A9 实现与集成** | Superpowers subagent development + TDD；gstack QA；OpenSpec apply；a11y/e2e agents | `development.tdd` + repo-native tools；条件 `qa.browser`；native RED/GREEN/REFACTOR fallback | 新版强调垂直切片和真实边界，避免把 browser QA 当后端集成测试；但淡化了 subagent 双审查和 OpenSpec artifact continuity | **部分合理** | 单元/服务代码优先 Superpowers TDD 或等价 TDD skill；计划稳定且任务独立时用 subagent-driven development；OpenSpec 项目用 apply；后端集成跑原生测试；可运行 Web UI 才用 gstack QA/Playwright；a11y 随 UI 风险触发 |
| **A10 审查** | Superpowers `requesting-code-review`/`receiving-code-review` + gstack `review` +语言 reviewer | `review.code`；按风险 security/accessibility/performance/database | 新版把专项审查与真实风险相连，避免“技术出现即全套 reviewer”；旧版独立上下文、精确 diff 范围和反馈处理方法更具体 | **合理，但应恢复 provider profile** | 通用独立 review：仓库 code-review skill 或 Superpowers requesting review；pre-landing 深审可用 gstack `review`；语言 reviewer 仅在其规则适配时；高风险必须独立上下文。注意 gstack `review` 可能 auto-fix，不是纯只读 |
| **A11 PR 与变更证据** | gstack `ship`，随后 `land-and-deploy` | `review.code` + `delivery.release`；PR template/CI/local review record | 新版允许无 PR 的本地/嵌入式项目，并要求可重构证据；也避免在“管理 PR”步骤隐式合并部署 | **明显合理** | GitHub/GitLab 原生命令与 CI artifact 优先；用户明确要求 ship 且 gstack 已配置时用 `ship`；`land-and-deploy` 移到 A13，并要求外部写/合并/部署授权 |
| **A12 验证汇总** | gstack `qa-only` + `cso`；Superpowers verification；Lighthouse；a11y/performance agents | 确定性项目命令；条件 `qa.browser`、security/accessibility/performance reviewers | 新版按适用性收集证据，避免每个项目都做 Web、OWASP、WCAG、Lighthouse、k6；但“完成声明前新鲜证据”值得写成默认纪律 | **明显合理，建议恢复 verification provider** | 核心：项目 test/build/lint/typecheck；完成声明前使用 Superpowers verification 或等价 gate；Web 才用 qa-only/Playwright；安全、a11y、性能由风险/目标触发；保留 failed/blocked/stale/N/A 而非只写 pass |
| **A13 发布与恢复** | gstack `ship → land-and-deploy`；固定 5%→50%→100% canary | `delivery.release`；repo CLI/CI/deploy scripts | 新版支持不同平台、批处理、桌面/移动、无生产交付，并把 artifact digest、兼容性和 recovery 作为证据；固定百分比/10 分钟无流量和风险依据 | **明显合理** | 平台原生发布/runbook 优先；gstack 配置完备且用户授权时 `land-and-deploy` 很好用；rollout cohort/窗口必须按流量、风险、可逆性决定，不照抄固定比例 |
| **A14 观察** | gstack `canary`；Sentry/Datadog/Grafana | `operations.monitor`；项目 logs/metrics/traces/audit | 新版覆盖基础设施、应用、业务、安全和 UX，并要求 baseline/阈值/窗口；gstack canary 强于页面、console 和截图，但不能代表全部生产健康 | **合理** | 项目 observability/SLO 为主；Web 视觉/console/perf 回归用 gstack canary 补充；无告警不等于成功，必须关联 REQ/NFR 与 cohort |
| **A15 学习与反熵** | gstack `retro` + `document-release` | `operations.retro`；main agent 查 Git/incident/metric/support | 新版适用于 incident retro、单次 release learning、技术债和临时机制清理；旧版 weekly/team trend 与文档同步更具体 | **合理，但建议恢复两个 provider** | 周/迭代团队复盘用 gstack retro；发布后文档漂移用 document-release；事故用项目 incident/postmortem 模板；所有 action 必须有 owner/date/origin，并回写测试、规则或 runbook |

## 五、哪些旧说法不应原样恢复

### 5.1 “三套系统组合 = 完整全栈流程”证据不足

v1.0 的 coverage 星级和 “45%/80%/95% contribution share” 没有评测方法、样本或版本依据，属于主观评分。可以保留定性适配矩阵，但不应恢复伪精确百分比。

### 5.2 gstack 的来源链接错误且版本未固定

v1.0 README 把 gstack 链接写成 `https://github.com/icestarx`，并没有指向 gstack 仓库；依赖文档也只写 `~/.claude/skills/gstack/setup`，未记录来源、commit 或兼容版本。即使技能名正确，也无法复现当时所评估的合同。

### 5.3 固定 slash command 会漂移

OpenSpec 已从 `/openspec:*` 演进为 `/opsx:*`；gstack 在外部宿主可能暴露 `/gstack-*` 名称；Superpowers 在不同宿主可以显式调用、隐式触发或通过插件加载。仓库不应把某个调用拼写写入核心流程。

### 5.4 “required agent” 没有来源就是无效依赖

`architect`、`database-reviewer` 等通用名字存在多个实现。没有 source/version/description hash 时，运行结果不可预测。当前的 capability + discovery 比 v1.0 正确。

### 5.5 skill 不能替代确定性工具

skill 可以规定如何执行测试或审查，但测试通过、schema 有效、部署成功必须由项目 test runner、validator、CI、artifact registry 和 observability 证据证明。当前“repository-native deterministic commands 优先”应保留。

### 5.6 自动修复、提交、推送、合并和部署要分开授权

gstack 的 `qa`、`design-review`、`review`、`ship`、`land-and-deploy` 具有不同写入/外部副作用。v1.0 把它们作为步骤默认动作，容易把“要求审查/报告”扩大成“允许修改或发布”。推荐映射必须标注：read-only、workspace write、git write、remote write、production write。

### 5.7 当前缺少 completion verification 的一等能力

`development.tdd` 证明某个实现循环经历了 fail-before/pass-after，不等同于“准备宣布完成时，重新运行完整、相关且新鲜的验证”。当前 A12 虽要求确定性项目命令，但 capability catalog 没有承接 Superpowers `verification-before-completion` 的独立合同，也没有让 A9-A15 的所有完成声明共享同一 gate。

建议增加 `verification.completion`，要求：识别能证明声明的命令 → 现场完整运行 → 读取退出码和失败数 → 对照需求逐项核验 → 仅在证据支持时声明完成。Superpowers 是推荐 provider，main-agent + repository-native commands 是 fallback。

### 5.8 `delivery.release` 范围过宽

当前 `delivery.release` 的 required outcome 同时写了 PR、CI、rollout、health checks、recovery，并被 A8、A11、A13 重复使用。这会造成三个问题：

- provider 误匹配：`setup-deploy`、`ship`、`land-and-deploy` 实际合同不同；
- 权限混淆：准备环境、创建 PR、合并、生产部署不是同一级副作用；
- 证据混淆：CI result、artifact provenance、deployment record、rollback proof 不应折叠成一个模糊“release evidence”。

建议至少拆成 `delivery.environment`、`delivery.change-review`、`delivery.deploy`、`delivery.recover`；如果不拆 ID，也应为 A8/A11/A13 定义不同 sub-contract 和 side-effect guard。

## 六、建议的最终 provider 选择模型

### 6.1 保留当前能力合同

继续让 [process-steps.md](../references/process-steps.md) 描述 outcome/evidence/gate，让 [skills-mapping.md](../references/skills-mapping.md) 描述 capability，不把仓库重新绑死在 gstack、Superpowers 或 OpenSpec 上。

### 6.2 增加一个经验证的 provider registry

建议未来单独维护 provider profiles（不在本次研究中修改），每条至少包括：

```yaml
provider: superpowers.test-driven-development
capabilities: [development.tdd]
best_for: [feature, bugfix, refactor]
avoid_for: [throwaway-prototype, generated-code, config-only]
hosts: [codex, claude-code, ...]
discovery_names: [test-driven-development]
side_effects: [workspace-write]
requires: [native-test-runner]
source: https://github.com/obra/superpowers
verified_commit: 5bf4e78011075bcfc0dc295f0724994cd123ee71
verified_at: 2026-09-19
fallback: native RED/GREEN/REFACTOR loop
```

这比在 A 步骤正文直接写 slash command 更稳定，也比仅写抽象 capability 更好执行。

### 6.3 推荐优先级

每一步按以下顺序选择：

1. 用户或仓库明确指定且已经安装的 provider；
2. 项目原生命令与权威制品；
3. provider registry 中与当前场景、宿主和副作用授权匹配的首选技能；
4. 风险触发的专项 reviewer；
5. main agent fallback，并记录自动化/独立性/证据缺失。

### 6.4 建议恢复到文档中的具体 provider 矩阵

| 能力 | 推荐 provider（发现后调用） | 何时不用 |
|---|---|---|
| `product.discovery` | gstack `office-hours`；Superpowers `brainstorming`；OpenSpec `explore` | 需求已明确且有权威 ticket/PRD 时不重复 discovery |
| `product.scope-review` | gstack `plan-ceo-review` | 小 bug、纯维护或范围没有争议 |
| `product.requirements-review` | 专门 PRD/requirements review skill；本仓库 requirements workflow | 不用 discovery skill 冒充独立审查 |
| `design.system` | gstack `design-consultation`；UI UX Pro Max；项目 design system；Figma/design provider | 已有系统时不从零重建 |
| `design.prototype` | Figma/prototype skill、轻量 HTML 原型；适配时 gstack `design-html` | 后端-only；不要默认把 Pretext 输出当目标栈生产代码 |
| `design.review` | 实施前 gstack `plan-design-review`/Impeccable critique；live site 用 `design-review`/Impeccable audit | 不混淆 plan review 与 code-fixing visual audit |
| `architecture.review` | gstack `plan-eng-review`；可信 architect/codebase-design provider | 小局部变更不做全系统重设计 |
| `planning.decompose` | Superpowers `writing-plans`；OpenSpec tasks | 单文件机械改动不写超细计划 |
| `spec.change` | OpenSpec `propose/update/sync/archive` | 已有 RFC/ADR/OpenAPI/issue 体系足够时避免重复 source of truth |
| `database.review` | 来源/版本明确且数据库匹配的 specialist + 原生 migration tests | 无 persistence 变更；不要仅因项目“有数据库”就调用 |
| `development.tdd` | Superpowers TDD 或本地 TDD skill + 原生测试器 | 按 provider 规定处理 prototype/generated/config 例外 |
| `qa.browser` | gstack `qa`/`qa-only`、Playwright/browser skill | 非 Web 或没有可运行 UI；后端 integration tests 用原生命令 |
| `review.code` | Superpowers requesting review、仓库 code-review skill、gstack `review` | gstack review 有 auto-fix 时，纯只读请求需选其他 provider |
| `review.security` | gstack `cso` 或来源明确的 security review/scanner | 由风险触发；不要用“跑过通用 review”宣称完成安全审计 |
| `review.accessibility` | a11y specialist + axe/browser/键盘证据 | 无 UI 影响时 N/A |
| `review.performance` | Lighthouse（Web）或项目 load/benchmark 工具 + specialist | 没有目标/基线时先定义 NFR，不能只报一个分数 |
| `verification.completion`（建议新增） | Superpowers `verification-before-completion` + 项目 test/build/lint/typecheck | 不以旧运行、子 agent 自报成功或部分检查证明完成 |
| `delivery.environment`（建议拆分） | 项目环境/IaC/CI；gstack `setup-deploy` | 不因准备环境而推定允许创建 PR 或部署 |
| `delivery.change-review`（建议拆分） | 项目 PR/CI；gstack `ship` | 未授权 remote write 时只准备 PR 内容和本地证据 |
| `delivery.deploy` / `delivery.recover`（建议拆分） | 项目 CD/runbook；gstack `land-and-deploy` | 未授权 production write 时只生成部署/恢复计划 |
| `operations.monitor` | 项目 SLO/metrics/logs/traces；gstack `canary` 补充 Web 信号 | canary 截图不能替代业务/基础设施观测 |
| `operations.retro` | gstack `retro`、`document-release`；项目 postmortem/runbook 流程 | 不为极小变更强制召开完整团队 retro，但必须处置临时机制 |

## 七、最终判定

### 应保留的当前设计

- capability IDs 作为稳定接口；
- provider discovery 与缺失时 fallback；
- 原生命令优先生成确定性证据；
- 专项审查由风险触发；
- A6-A12 按垂直切片循环，而非模块批处理；
- PR、合并、部署、生产观测分开处理授权和证据。

### 应修正的当前设计

- 不再把 gstack、Superpowers、OpenSpec 统称为 Claude legacy；改为“跨宿主的可选第三方 providers”，分别记录支持矩阵。
- 在 `platform-adapters.md` 或独立 registry 中恢复场景化具体 provider 推荐。
- A1/A6/A9/A10/A12 明确列出 Superpowers 的优势和触发条件。
- A2-A3 恢复 gstack UI/UX 组合，并修正 `plan-design-review` 与 `design-review` 的阶段差异。
- A7 修正 OpenSpec 定位：change/spec artifact lifecycle，而不是默认 API contract generator。
- A8、A11、A13 对 gstack 技能标注副作用与授权边界。
- A12 新增 `verification.completion`，将“fresh verification evidence before completion claims”提升为通用 gate，但仍使用项目原生命令证明。
- 将过宽的 `delivery.release` 拆成 environment、change-review、deploy、recover，或至少定义等价的分步子合同。
- 所有 named agents 增加 source/version/contract；否则只保留 capability 名。

### 一句话答案

**不是旧版技能更好，也不是新版能力更好：新版的架构更正确，旧版的 provider 选择更有执行力。合理的修复是“保留新版 capability 合同，把 Superpowers、gstack UI/UX、OpenSpec 按正确场景重新挂回 provider 层”，而不是恢复 v1.0 的硬依赖和固定命令。**

## 八、证据与不确定性

### 仓库内证据

- v1.0：`25312e89dc71ef05b1fb9b96d256da6a8e5429f7`
- 首次 provider 抽象迁移：`aeee990abc95fcc11c372bdb30561fa39c56d51f`
- 当前 15 步路线：`f901148cdd5211ce74874fdc185bb81eff58c41f`
- 当前文件：[process-steps.md](../references/process-steps.md)、[skills-mapping.md](../references/skills-mapping.md)、[platform-adapters.md](../references/platform-adapters.md)、[DEPENDENCIES.md](../DEPENDENCIES.md)

### 外部一手来源快照

- Superpowers：commit [`5bf4e780`](https://github.com/obra/superpowers/tree/5bf4e78011075bcfc0dc295f0724994cd123ee71)
- gstack：commit [`a6b3a575`](https://github.com/garrytan/gstack/tree/a6b3a57512ca6d5c6aa5b68f74f736195021f96e)
- OpenSpec：commit [`bae58cf6`](https://github.com/Fission-AI/OpenSpec/tree/bae58cf61479986431bb798acbe5a688a591c18c)
- ECC named-agent 线索：[官方仓库](https://github.com/affaan-m/ECC)
- Codex skill 机制：[OpenAI 官方文档](https://developers.openai.com/zh-Hans/docs/build-skills)

### 不确定性

- v1.0 没有固定 gstack、Superpowers、OpenSpec 的版本，本文只能将历史引用与研究日的官方合同比较，不能证明 2026-05-16 当天每个命令的实现完全相同。
- v1.0 没有写 named agents 的来源；“来自 ECC”只是基于名称集合和目录约定的高概率推断。
- provider 的实际效果取决于模型、仓库、prompt、安装版本与权限。官方文档能证明合同和设计目标，不能证明其在所有项目上优于其他实现。
- 本报告没有对 provider 做同题盲测，因此不保留 v1.0 那种星级和贡献百分比；“更好用”的判断是按任务适配性、可移植性、证据质量、副作用和流程成本作出的工程评估。
