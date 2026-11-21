---
name: bounds-measure
description: "Vet a measured number before it is reported or acted on: latency, throughput, frame rate, memory, disk reclaimed, backtest or study results, eval scores, or usage counts. Use when producing or about to trust a speedup, regression, comparison, or result; not for finding a bug's cause or tuning a value judged by feel."
license: MIT
---

# Bounds measure

A number claims that specific work happened under stated conditions. Vet it before it reaches a PR, report, or decision. Measuring grants no authority to change, delete, or publish. The user's instructions may name private datasets, dashboards, or harnesses to use.

## Before running

Write the sentence you expect to report: "export p50 is 30% faster on the 60k-row dataset." Name the decision it informs and the result that would change it. Read the measurement script or query: what it times, counts, filters, and ignores. Record revision, environment, data, and machine load; on a busy machine, interleave the sides and say so.

A requested ballpark needs one labeled run, still checked for errors and work done. A choice between options is never a ballpark. Before reusing a harness, prove it separates a known-bad case from an easy one and prints error and work counts, then freeze it.

## Check the number

Answer each that applies from a run, not code reading. Limiter, tuning, and repeatability apply to comparisons and performance numbers; for a single count or total, [checks by kind](references/checks.md) says what replaces repeat runs.

1. **Limiter:** why is it not twice as good? Name the bounding resource from a profile or counters in an unreported run.
2. **Tuning:** each side runs as production would, with the same builds, settings, caches, versions, and data.
3. **Bounds:** do the arithmetic against bandwidth, cores, totals, and the changed part's share. A result past a bound measured something else.
4. **Errors and skips:** count failures, timeouts, retries, skipped items, and wrong outputs.
5. **Repeatability:** at least five alternating runs per side, with median and range. A gap within the spread is no measurable difference.
6. **Relevance:** measure the end-to-end path the decision depends on; give a micro result as its share.
7. **Work happened:** confirm counts and outputs inside the measured region, such as rows written or files removed.
8. **Denominator:** name what is counted over what population: events or jobs, users or sessions, gross or net, before or after exclusions. Both sides must match.

## Report

Lead with the verdict: for a comparison, better, worse, no measurable difference, or inconclusive; for a single value, holds, does not hold, or inconclusive. Give unit, denominator, run count, median and range, exclusions, limiter, environment, and revision: "p50 41 ms to 33 ms, median of 7 alternating runs, range 32 to 35 ms, bound by JSON parsing on one core."

Call it inconclusive when a comparison's limiter is unknown, a side ran untuned, or errors, work done, or the denominator went unchecked; name the gap. Label estimates. Put one primary number in a PR or post; link the runs.
