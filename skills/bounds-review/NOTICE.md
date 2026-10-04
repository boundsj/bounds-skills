# Attribution

This is a Bounds adaptation, not an upstream installation.

- Matt Pocock, MIT: https://github.com/mattpocock/skills/tree/24fe0ef7737efae15c87225755e9f6f5965e4888
- Lauren Tan, pstack, MIT: https://github.com/cursor/plugins/tree/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack

Adaptations preserve concise planning, reproducible debugging, evidence-based review,
structural improvements, conditional documentation, and local verification. Bounds
removes mandatory tracker setup, seam approvals, broad mode hooks, Cursor-specific
metadata and fixed model choices. Scope and permissions come from the user's task.

## bounds-review

Selected source material: Pocock `code-review`; pstack `interrogate`.

Adaptation: Checks requirements, maintainability and correctness. Pins revisions, supports local snapshots, defaults to one warranted independent reviewer and bounds re-review. Removes model tables and unconditional fan-out.

Full license notices are in [LICENSE.txt](LICENSE.txt). This source mapping travels
with the installed revision; no link to a moving branch is required.
