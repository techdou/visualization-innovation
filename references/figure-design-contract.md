# Figure Design Contract

For each major figure/view specify:

## Figure role
Method/architecture, exploratory analysis, explanatory result, comparison/ablation, interaction sequence, design space/taxonomy, evaluation, or narrative.

## Analytical question
Write one concrete judgment the figure should support.

## Evidence contract
Unit of analysis, aggregation, baseline/reference, uncertainty/missingness, raw evidence path, and transformations.

## Visual contract
For each important variable: mark/channel, why that channel, and tradeoff.

## Interaction contract
`intent → trigger → target → state transformation → feedback → analytical consequence`

## Cross-panel contract
Shared state such as selected IDs, filter, order, parameter, comparison pair, time range, focus, or history state.

## Reading order
Specify first fixation and next 2–4 visual steps. Use layout/annotation/alignment rather than arbitrary arrows where possible.

## Story sentence
> Start at ___ to establish ___; move to ___ to reveal/compare ___; inspect ___ to verify ___; conclude/continue with ___.

## Innovation claim
State exactly what changes: encoding, layout, interaction, coordination, story, authoring, or medium.

## Failure modes
Clutter, occlusion, misleading distance/area, color overload, ordering instability, hidden uncertainty, scale sensitivity, hard-to-learn glyphs, interaction discoverability, weak evidence traceability.

## Caption rule
Captions should explain what each panel contributes to the argument and how evidence should be read, not merely list A/B/C components.

For important cross-view actions apply `references/coordination-contract.md`: specify typed selection, mapping, population, invariant reference, undo, and async version policy.
