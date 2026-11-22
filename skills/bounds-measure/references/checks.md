# Checks by kind of number

Load only the section for the number at hand. Every section still needs the verdict, unit, denominator, and exclusions from the report rules. Run count, range, and limiter apply where runs repeat or sides are compared; each section names what replaces them otherwise.

## Performance: latency, throughput, frame rate, memory

- **Limiter:** use CPU per process (`top`, `pidstat`), a runtime profiler (`perf`, `py-spy`, `node --cpu-prof`, or the platform's profiler), I/O wait, and syscall counts, then map the hot spot to source. Profile in a run you do not report, because profilers slow the work. Watch the load generator; if it saturates first, you measured it. If a change did not move the number, the limiter explains why.
- **Tuning:** release builds, production flags and environment, batching and transaction settings, connection pools, and caches as warm or cold as production sees them. A limiter that is a setting (a commit per row, a debug build, a missing index) means that side is untuned. Tune it and measure again before picking a winner.
- **Bounds:** compare bytes per second with disk and network bandwidth, and operations per second times cost per operation with available cores. Removing a piece that takes 10% of a run can make the run at most about 11% faster. A display refreshing at 60 Hz cannot show more than 60 frames per second.
- **Work happened:** lazy code (generators nobody iterates, promises nobody awaits, results a compiler or JIT can discard) and timeouts produce numbers for work that never ran.
- **Frame rate:** report frame-time percentiles or dropped frames over a fixed interaction on the device class that matters, not a simulator average.
- **Memory:** separate peak from steady state and resident from allocated; repeat the cycle several times to show whether growth is a leak.
- **Close calls:** use a rank-sum test or the harness's own statistics. Stop adding runs when the spread is larger than the effect, and report no measurable difference.

## Evals and model comparisons

- Confirm every run did the task from its outputs or transcript, not its self-report. Count failed, refused, truncated, and timed-out runs.
- Check that a gap holds across trials, tasks, and models; report per-task results, not only a mean.
- Blind the comparison. Candidates get an organic task with no evaluation wording and do not learn other candidates exist. The judge sees sanitized labels, never model names, scores all outputs in one pass on one scale, and comes from a different model family when one is available. Keep the rubric from candidates.
- Read the outputs yourself and compare with the judge. Disagreement means a biased judge or an ambiguous rubric.
- Ask whether the scenario matters to the decision being made.

## Backtests, studies, and forecasts

- Freeze the data snapshot, code revision, metric, and success threshold before looking at results.
- Keep evaluation data out of tuning. Check for look-ahead: no input may use information unavailable at decision time. Report in-sample and out-of-sample results separately.
- Include costs such as fees, spreads, slippage, latency, and limits; report gross and net.
- State the population: survivorship, excluded or missing records, and base rates. Compare with a simple baseline.
- Count the variants tried. A best-of-many result needs a fresh holdout before it is claimed.
- Give the sample size and an interval, not only a point estimate.
- In place of repeat runs for a deterministic backtest: out-of-sample results plus the count of variants tried.

## Disk and storage

- Measure free space on the volume before and after, plus per-item sizes. An estimate of reclaimable space is not space freed; report both, labeled.
- File sizes can differ from space reclaimed because of clones, hard links, sparse files, compression, and snapshots. Deleted space can stay held by snapshots, open files, or a trash folder.
- State units: GB (10^9 bytes) or GiB (2^30 bytes). `df -h` and `du -h` print powers of 1024; `df -H` and Finder use powers of 1000.
- In place of repeat runs: free space on the same volume immediately before and after, with nothing else writing large files in between.
- Confirm deletion happened, and note what regenerates, such as build caches.

## Usage and telemetry

- Define the event and the counted entity: events, unique users, sessions, or jobs.
- State the window and timezone; exclude partial periods and allow for ingestion delay.
- Name exclusions: test, internal, automated, and duplicate traffic, and any sampling rate.
- A new event or a changed definition is an instrumentation change, not a usage change.
- Compare like periods, allowing for weekday mix, seasonality, and release dates.
- In place of repeat runs: the exact query, window, and filters, so the count can be rerun and match.
