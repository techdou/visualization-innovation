# Coordination contract — shared handoff v1

Use this same contract in both skills: innovation proposes analytical operations; RVA audits their meaning. This is an engineering schema, not a library-specific API. Both bundles contain the same reference and template to remain independently usable.

## Link semantics

| Kind | Meaning | Required caution |
|---|---|---|
| Identity | Locate the same entities elsewhere | Stable keys; specify one-to-many and missing matches |
| Condition | Filter/reaggregate by a predicate | State base population and denominator changes |
| Comparison | Pin A; select B; compute differences | Snapshot versus live predicate, overlap and paired units |
| Derivation | Create a new view/dataset from state | Persist parent state and transformation |
| Parameter | Change an analytical condition | Distinguish stored lookup, simulation and actual recomputation |
| History | Restore/compare prior states | Restore data/computation versions or mark unreplayable |

Use typed selections: `none` (no active selection), `empty` (active query matched nothing), `ids`, `predicate`, `range`, or `geometry`. Never equate `none`, `empty`, and all records. Convert geometry to domain-space predicates/IDs using the correct coordinate system.

## Contract fields per important link

- ID and analytical intent; source and target view IDs.
- Selection kind, entity grain, key(s) and coordinate/unit semantics.
- Mapping cardinality, missing-match behavior, deduplication and aggregation.
- Operator: highlight, filter, aggregate, compare, derive or recompute. State whether the operation uses cached outputs, simulation or a real model.
- Cross-selection combination: replace/union/intersection/difference; specify order for noncommutative operations.
- Base population, displayed denominator and source-filter inclusion/exclusion. Name the reason for self-filter exclusion where used; do not blindly apply every filter to every panel.
- Invariants: pinned cohort, scales, sort order, reference range, color meaning and version consistency.
- Target feedback: counts, active conditions, loading/empty/error/stale states and accessible controls.
- Clear, undo and redo semantics; scope reset separately from clearing one selection.
- Event origin and transaction/version ID; allow one logical action to commit once. Derived view updates must not loop back as fresh user actions.
- Async policy: cancel or ignore stale responses; bind results to query/model/data version; never mix an old result with new control labels.
- At least one non-default action trace with expected entities/counts/metrics; use a tiny inspectable fixture for exact assertions.

## Example

Source selects samples s1,s2 from a disagreement view. Map by sample_id into a sample-label membership table where s2 has two labels. Target sample count is 2; label membership count may be 3. These are different denominators. Pin A as IDs plus dataset version; later changing B must not silently redefine A. Distinguish fixed membership with recalculated metrics from a frozen historical result that also retains model/parameter/result versions. Show overlap if A and B share samples.

## State architecture

Data + version → transformation specification → analytical state → query/derived view models → renderers. Let input commands change state; do not let views independently mutate source data. Store semantic selections rather than pixel bounds when layout can change. Persist consequential states only; full history is optional.

## Acceptance checks

Select → inspect → pin A → change B → compare → clear B → undo → replay. Include no-match, partial missing keys, many-to-many mappings, rapid parameter edits, delayed responses, and a dataset version change where relevant. Freeze scales or visibly label rescaling. Verify the exported state agrees with the screen. The contract linter checks completeness and references only; execute tests against the actual application to verify behavior.

## Primary implementation leads

Checked 2026-09-28: Vega-Lite parameters support selection-driven encoding/filter/domain changes (https://vega.github.io/vega-lite/docs/parameter.html); Mosaic core separates clients, selections and coordination (https://idl.uw.edu/mosaic/core/). The broader contract above is this skill's synthesis, not a promise these libraries implement every rule automatically.
