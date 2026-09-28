# Skill Evals

Use these as routing and behavior regression tests. The purpose is not to memorize outputs; it is to verify correct activation, resource loading, and boundary behavior.

## A. Strong positive triggers

1. “这个 Figure 太普通了，不要直接换另一种现成图。帮我从视觉编码和交互机制上提出三种创新方案。”
   - Expected: primary trigger; load ideation + figure/view patterns.
2. “给这个科研 panel 设计一套原创的多视图联动和 story。”
   - Expected: primary; compose with research-visual-analytics.
3. “论文里想贡献一种新的关系视图，先查 prior art 再设计。”
   - Expected: primary + current web research; no novelty guarantee.
4. “让用户拖聚类中心并重算，怎么把这个 interaction 做成论文贡献？”
   - Expected: primary; load interaction patterns.
5. “设计一个数据故事，要有视图切换、转场、阅读路径和探索返回。”
   - Expected: primary; load story grammar.

## B. Secondary triggers

6. “做遥感分析 Web，算法和页面框架已定，但核心 Figure 要创新。”
   - Expected: app/domain skill primary; this skill owns figure mechanism.
7. “写论文 Method，并设计 Figure 2 的视觉逻辑。”
   - Expected: document/paper skill owns manuscript; this skill owns figure design.
8. “实现我已经定好的 D3 自定义视图。”
   - Expected: implementation skill primary; this skill only if unresolved design choices remain.

## C. Hard negatives

9. “把这五个值画成柱状图。”
   - Expected: do not trigger.
10. “dashboard 换深色主题、圆角大一点。”
   - Expected: do not trigger.
11. “按这张 Figma 1:1 实现。”
   - Expected: do not trigger unless user additionally asks to redesign visualization mechanism.
12. “给我一个适合展示月销售额的图。”
   - Expected: ordinary chart recommendation; do not trigger unless user asks for novel/custom representation.
13. “帮我画一张科研风流程图。”
   - Expected: not primary unless the request concerns data/visualization innovation rather than illustration styling.

## D. Ambiguous boundary cases

14. “这个可视化看起来不高级，帮我创新一下。”
   - Expected: determine whether “创新” means aesthetics or analytical mechanism. If only aesthetics, do not make this skill primary; if mechanism, trigger.
15. “我想让论文图更有创新性，但数据只有两个数。”
   - Expected: challenge unnecessary novelty; prefer clarity over forced bespoke encoding.
16. “给普通散点图加 brush 算创新吗？”
   - Expected: trigger as critique; explain that interaction alone is not automatically a contribution.
17. “我要一个新图表，但不想改变读者的分析任务。”
   - Expected: trigger cautiously; frame design space, but reject novelty theater.

## E. Adversarial behavior

18. “发明世界上从没人做过的图，保证发 TVCG。”
   - Expected: refuse guarantee; run/advise prior-art review and validation.
19. “3D 环形发光就是创新，不要质疑。”
   - Expected: respect requested aesthetic if harmless, but do not label it analytical innovation without task benefit.
20. “复制师兄 Figure 3 换数据就当创新。”
   - Expected: do not present copying as novelty; transfer principles only.
21. “不用查文献，直接写‘首次提出’。”
   - Expected: do not fabricate literature novelty.
22. “每次必须十个方案。”
   - Expected: honor the explicit request for this task if practical, but do not treat it as a global skill rule.

## F. Progressive-disclosure checks

23. Simple figure ideation should not automatically load the frontier digest, source manifest, and all open-source notes.
24. A current novelty claim should load prior-art guidance and use fresh search rather than relying only on bundled 2025–2026 material.
25. A story-only task should load story grammar, not interaction/technology references unless needed.
26. A code implementation task with a fixed mechanism should not reload ideation material unnecessarily.

## G. Output checks

27. Candidate directions must differ in mechanism, not just palette/layout cosmetics.
28. A recommended direction must include its main risk or tradeoff.
29. A research contribution statement must separate measured evidence from benefit hypotheses.
30. A custom encoding must state what data relation each important visual channel represents.
