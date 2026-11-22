---
name: bounds-debug
description: "Reproduce an observed bug or performance regression, isolate its cause, fix it within scope, and verify the user's failing behavior with a repeatable check."
license: MIT
---

# Bounds debug

Identify the expected and observed behavior, trigger, affected revision, and environment. Inspect enough code and existing tooling to construct a fast check of the user's symptom. Prefer a real public interface: a test, CLI fixture, request, or driven UI action.

Run the check before changing behavior. Confirm it fails for the reported reason; a missing dependency or unrelated crash is not reproduction. Minimize inputs when that helps isolate the cause. For intermittent failures, record attempts and failures; for latency, record workload and baseline conditions. Read [feedback loops](references/feedback-loops.md) when the check is difficult or noisy.

Use falsifiable hypotheses and the smallest probe that distinguishes them. One obvious cause needs no ceremonial hypothesis list. Broader uncertainty may justify ranked alternatives, targeted instrumentation, or bisection. Follow the failing data or state across relevant boundaries before broadening the change. Confirm a probe is installed and producing output before reading its silence as evidence; a command chain that continued past the install step does not prove it.

Fix the cause within the authorized scope. Preserve unrelated behavior. Where practical, keep a regression check that demonstrably fails before the fix and passes afterward. If you force that failure by mutating code or a fixture, diff against a pristine copy to prove the mutation landed before trusting the failure. Assert the result a user observes against an independently known expectation; avoid tests that mirror the implementation.

Rerun the original scenario and relevant neighboring checks. Remove temporary instrumentation and clean up only resources created for this investigation, preserving useful redacted evidence.

Report the cause, change, commands/results, and coverage limits. If reproduction is unavailable, report attempts and the missing input or capability. Source inspection may support a hypothesis or a clearly labeled tentative fix; it does not prove the reported bug is resolved. Stop speculative retries when they no longer add evidence.
