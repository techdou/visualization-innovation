# visualization-innovation

[English](README.md) | [中文](README.zh-CN.md)

An Agent Skill for **mechanism-level innovation in research visualization**: chart redesign (图表二创), new chart families, interaction and coordinated-view innovation, evidence-based visual stories, and prior-art-aware novelty claims.

The skill designs **useful, testable mechanisms** out of analytical problems — not styling polish. Data semantics and research integrity are hard-constrained: no unverified first-ever/SOTA claims, stored-query vs. simulation vs. real recomputation kept distinct, and bundled literature leads must be reverified against primary sources before citation.

## When it triggers

- Redesign a reference chart (decompose → inherited/changed/gained/cost ledger)
- Invent a new view or chart family (visual grammar + decoding rules + baseline comparison)
- Generate mechanism-distinct alternatives (Familiar+ / Recombined / Speculative divergence)
- Design interaction and linked views (testable cross-view link contracts)
- Organize panel layouts (complementary evidence roles and dependency maps)
- Assess publication novelty (prior-art search ledger + bounded claim)

The SKILL.md description carries Chinese and English trigger keywords (图表二创 / 新视图 / 交互创新 / 多图联动创新) for automatic agent routing.

## Layout

```
SKILL.md                  # Entry: routing table + workflow + guardrails
references/               # Task-scoped methodology docs (anti-patterns, rubrics, prior-art search)
assets/                   # Candidate card / design brief / coordination-contract templates
scripts/                  # See below
agents/openai.yaml        # Agent-platform metadata
```

## Scripts

Python 3, no third-party deps (`validate_skill.py` needs PyYAML):

```bash
python scripts/scaffold_innovation_brief.py --help   # Copy the design-brief template
python scripts/score_candidates.py --help            # Diagnostic candidate triage (gates, no auto-ranking)
python scripts/validate_skill.py <skill_dir>         # Structural skill validation
python scripts/package_skill.py --help               # Export packaging
```

## Install

```bash
git clone https://github.com/techdou/visualization-innovation.git ~/.agents/skills/visualization-innovation
```

Or unzip a release into `~/.agents/skills/`. Restart your agent session to activate.

## Companion skill

Pairs with [research-visual-analytics](https://github.com/techdou/research-visual-analytics): this skill owns innovative design, the companion owns correctness and evidence review. Both share the coordination-contract template and also work standalone.

## License

MIT
