# Candidate Evaluation Rubric

Use qualitatively by default. Numeric scoring is optional and should support, not replace, design judgment.

## Gating criteria

A candidate should not advance if it fails any of these materially:

1. **Task fit** — does it support the target judgment?
2. **Evidence gain** — does it reveal/verify something the baseline makes difficult?
3. **Perceptual clarity** — can the intended relation be decoded without excessive training?
4. **Scientific honesty** — are uncertainty, transformations, and limitations represented appropriately?

## Differentiation criteria

5. Mechanism differentiation
6. Interaction value
7. Coordination value
8. Story/read-order coherence
9. Learnability/discoverability
10. Scalability
11. Implementability
12. Reproducibility
13. Evaluation tractability
14. Prior-art separation

## Optional 0–4 scale

- 0 — fails / unsupported
- 1 — weak
- 2 — acceptable
- 3 — strong
- 4 — contribution-defining

Never select a candidate solely because it scores highest on novelty. Prefer strong **task fit × evidence gain**, subject to adequate perceptual clarity and feasibility.

## Review output

For the leading candidate, always state:

- strongest reason to keep it;
- most serious failure mode;
- what evidence would falsify the claimed benefit;
- what should be prototyped first.

## Gate decisions and optional script

Mark each gate pass/fail/unknown with a reason. Known material failure blocks advancement; unknown blocks acceptance pending evidence. In optional numerical triage, scores 0–1 fail a gate, 2–4 pass provisionally. All four gates include scientific_honesty. Unscored optional dimensions are unknown/not applicable, not zeros. Never use an average to offset a gate failure.

`scripts/score_candidates.py` accepts a JSON object mapping candidate names to criterion score objects. Recognized keys: task_fit, evidence_gain, perceptual_clarity, scientific_honesty, innovation, interaction_value, coordination_value, story_coherence, learnability, scalability, implementability, evaluation_tractability, reproducibility, prior_art_separation. Use finite numbers 0–4 or null (unknown). Only eligible candidates receive a diagnostic mean; held/rejected candidates are not ranked as winners. Numbers are assessor judgments, not measured evidence or automatic recommendations.
