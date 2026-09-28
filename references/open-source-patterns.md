# Open-Source Visualization Patterns

Public repositories were inspected for architecture/interaction ideas. Transfer abstractions, not source code or visual identity.

## Microsoft Data Formulator — `microsoft/data-formulator`
Iterative authoring, blended GUI+NL intent, Data Threads/branchable history, editable outputs. Transfer: model creative analysis as a graph/thread of states rather than one-shot generations.

## Ideas-Laboratory Libra — `Ideas-Laboratory/Libra`
Source organization separates layers, instruments, interactors, transformations, services, commands, and history. Transfer: keep interaction logic modular and separable from base visualization; compose primitives into richer behaviors.

## CMU DIG Divisi — `cmudig/divisi-toolkit`
Couples subgroup discovery with an interactive client and task-specific Subgroup Map for overlap/coverage. Transfer: if an analytical operation is novel, design a view that exposes its internal relation directly.

## Apple Amplio / interactive data augmentation
Public CHI 2025 project. Combines embedding-space visualization with actions that generate data in sparse/empty regions. Transfer: link visual metaphor to an actionable operation.

## GistVis — `ruishizou/GistVis`
Monorepo with reusable word-scale visualization package and demo; semantic extraction stages are separated from visualization. Transfer: decouple semantic extraction from rendering; build reusable micro-visual components.

## Vega-Lite — `vega/vega-lite`
Declarative grammar compiles marks, encodings, transforms, compositions, and selections. Transfer: when reuse/systematic variation matters, express innovation as a grammar/specification rather than hard-coded chart logic.

## Mosaic — `uwdata/mosaic`
Coordinator centralizes clients, selection updates, query management, caching, consolidation, and pre-aggregation. Transfer: use shared analytical state/query coordination instead of pairwise event wiring.

## Charticulator — `microsoft/charticulator` (archived)
Direct manipulation and layout-aware bespoke chart construction. Transfer: custom charts can be authored through constraints, handles, glyph/layout primitives, not code-only specification.

## General code-design lessons
1. Separate data transformation, analytical state, view rendering, interaction, and history.
2. Keep stable data IDs across views.
3. Express interaction state semantically where possible.
4. Make transformations deterministic/reproducible.
5. Prototype the novel mechanism in isolation before building the whole app.
6. Preserve a path from aggregate view to raw evidence.
