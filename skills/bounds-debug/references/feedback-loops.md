# Choosing a feedback loop

Use the cheapest check that reaches the actual failure. A public function or CLI fixture can be enough; UI state, concurrency, and persistence often require a wider path. Keep setup reusable and inputs isolated.

- **No test reaches it:** replay a redacted request or trace, use the project's browser/device harness, or create a small temporary driver. Mark any mocked boundary and what it prevents you from proving.
- **Intermittent failure:** fix the workload and seed when possible. Compare failure counts over a bounded number of attempts before and after. Zero failures in a sample is evidence with a sample size, not a guarantee.
- **Performance:** use the same workload and environment for baseline and candidate, account for warmup and noise, and report the measurement distribution or range. A single fast run is weak evidence.
- **Remote-only failure:** inspect accessible logs or a sanitized capture. Explain exactly which action remains unexecuted; request the smallest missing capability only if it blocks progress.

Before keeping a check, verify that it would reject the original defect. Assertions such as “did not throw” or “returned something” usually miss a wrong result. Scope instrumentation to a hypothesis and remove it when the probe ends. Do not log credentials or whole user datasets to make a loop convenient.
