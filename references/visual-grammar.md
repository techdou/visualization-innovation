# Generate and decode a visual mechanism

Use a constrained design space, not a random Cartesian product.

| Primitive | Design decision | Compatibility check |
|---|---|---|
| Data relation | comparison, set overlap, topology, transition, hierarchy, field | Does the data contain this relation? |
| Task | detect, rank, compare, trace, explain, verify | What must be directly readable? |
| Transform | difference, ratio, aggregation, projection, alignment | Preserve units, population and provenance |
| Marks/channels | point, line, region; position, length, color, shape | Match variable type and required precision |
| Space | axes, anchors, containment, ordered lanes, local lens | Define distance, area, direction and distortion |
| Operation | select, pin, compare, derive, steer, annotate | Specify typed state and evidence consequence |
| Coordination | identity, condition, comparison, derivation, history | Specify mapping and retained reference |

## Generative procedure

Choose 2–3 axes that address the bottleneck. Sketch genuinely different mechanisms; reject incompatible combinations early. Write a decoding rule before polishing the shape. Keep a standard detail/table view for exact retrieval when the custom view supports pattern recognition.

For each candidate answer:
- What entity does one mark represent? What does its absence mean?
- Which attribute maps to each channel, through which scale/transform?
- Which comparisons are valid? Which apparent distances/areas are not metric?
- What changes under selection, sorting, filtering or zoom? What stays fixed?
- How does a user read one example and verify it against source values?
- How do empty, tied, missing, signed, skewed and dense data behave?

## Claiming a chart family

A custom instance is sufficient for many projects. Claim a candidate reusable family only after specifying a grammar, constraints, decoding rules, failure envelope and at least two meaningfully different data/task instances. Evaluate transfer of the mechanism rather than renaming the same chart. This establishes generality evidence, not literature novelty.

## Prototype acceptance

Provide a worked decode example; preserve monotonicity when a channel represents magnitude; check permutation stability when ordering is not meaningful; demonstrate access without color alone; and show a static fallback when exporting an interactive view. Human comprehension remains an empirical question.
