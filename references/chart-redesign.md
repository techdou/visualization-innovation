# Reference chart decomposition and redesign

Treat a reference as evidence of a mechanism, not permission to assume its data semantics. Inspect the caption, legend, methods and interactive behavior when available. Record unknowns instead of inferring them from appearance.

## Procedure

1. Inventory entities, grain, variables, units, transformations and relations.
2. Decode marks/channels, axes, ordering, containment and meaningful versus decorative geometry.
3. Separate selection, filtering, derivation, model execution and visual feedback; a screenshot cannot establish hidden behavior.
4. Name the task bottleneck with one concrete query the current design cannot answer well.
5. Keep a competitive version of the reference as baseline. Improve labeling/standard interactions fairly in both conditions.
6. Change the mechanism carrying the bottleneck: difference encoding, uncertainty, local expansion, ordering, anchored comparison, semantic selection or derived view. Preserve other invariants so the source of any benefit is interpretable.
7. Compare inherited mechanism → changed mechanism → new analytical capability → reading/interaction/computation cost → falsifying test.

## Example: matrix of model disagreement

Baseline: a labeled pairwise matrix, sorting, tooltip and record drill-down. Limitation: a selected pair's aggregate disagreement hides which samples account for it and how their class composition differs from a reference.

Familiar+: retain matrix, pin pair and show aligned conditional distributions.
Recombined: form a reusable cohort from the pair's disagreement set; compare against a frozen cohort with overlap/support visible.
Speculative: locally expand a cell into a compact sample-by-condition micro-matrix while keeping row/column context. Test decoding and clutter before adding it globally.

Do not claim the familiar linked distribution or cell expansion is new to literature. Test whether cohort persistence or the custom encoding adds value beyond the strong baseline.

## Boundaries

- Give attribution for the reference and specify what was changed.
- Do not call faithful reproduction a research contribution.
- Do not manufacture uncertainty, causal edges or sample-level data absent from the source.
- Respect exact reproduction requests; distinguish reproduction from innovation rather than refusing ordinary replication.
- Report when the reference already solves the task better; a redesign may conclude with retaining it.
