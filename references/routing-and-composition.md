# Routing and Skill Composition

The goal is to avoid both under-triggering and “visualization” over-triggering.

## Primary

Use `visualization-innovation` as primary when the user asks to **invent, differentiate, or critique the mechanism** of a visualization:

- “这个 Figure 太普通，帮我设计新的视觉编码。”
- “不要套 ECharts 现成图，给我三种交互式关系视图方案。”
- “多 Panel 之间怎么形成新的协同分析机制？”
- “帮我把结果组织成有阅读路径的可视 story。”
- “这个可视化能不能作为论文贡献？先查 prior art。”

## Secondary

Use as a secondary design skill when another skill owns the deliverable:

- paper/document skill owns manuscript; this skill owns figure/visual contribution;
- web/app skill owns production implementation; this skill owns unresolved visualization mechanism;
- domain/science skill owns semantics/algorithm correctness; this skill owns representation/interaction/story innovation;
- `research-visual-analytics` owns analytical rigor; this skill owns ideation and differentiation.

## Do not trigger as primary

- simple chart request: “把这五个数画成柱状图”;
- styling request: “dashboard 换成深色/更高级”;
- generic UI layout request with no analytical visualization problem;
- faithful implementation: “按这张 Figma 原样做”;
- ordinary chart recommendation where novelty is not requested;
- image/illustration aesthetics unrelated to data representation.

## Boundary with `research-visual-analytics`

| Request | Primary | Secondary |
|---|---|---|
| Design a sound research VA workspace | research-visual-analytics | visualization-innovation only if novelty requested |
| Invent a new relation view | visualization-innovation | research-visual-analytics for rigor review |
| Review whether a custom view is misleading | research-visual-analytics | visualization-innovation for alternatives |
| Turn a paper result into a novel multi-panel Figure | visualization-innovation | research-visual-analytics |
| Implement a fixed VA design | implementation/web skill | research-visual-analytics only if design issues remain |

## Composition order for research-grade innovation

1. Domain/source grounding: define what the data and task actually mean.
2. `visualization-innovation`: frame limitation, design space, candidate mechanisms, story.
3. `research-visual-analytics`: audit task fit, perception, evidence traceability, uncertainty, coordination.
4. `visualization-innovation`: revise and articulate the contribution boundary.
5. Implementation skill: build and test the selected mechanism.

Explicit user instructions override this default ordering when they already specify a stage or output.

## Shared handoff and stopping rule

Innovation owns invention; RVA owns analytical correctness. Transfer one record containing question/view/link/state IDs, mapping/decoding rules, coordination contract, known facts, baseline and validation status. If the companion is absent, apply the core integrity checks locally. For fixed implementation, do not rerun ideation. Reopen a design only for a concrete unresolved risk; no automatic infinite review loop.
