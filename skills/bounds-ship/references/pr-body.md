# PR body

Write for a reviewer who has not seen the work. Skip preambles and keep prose brief.

- **Problem and result:** lead with the problem and the behavior after the change.
- **Shape, when it helps:** the smallest view that makes the key point clear, such as a diff sketch, call tree, or file tree. Omit it for a small change.
- **Evidence:** what shows the change works on the final head: before and after output, a failing then passing check, or a screenshot for a visual change. State coverage limits and checks not run.
- **Merge danger:** whether the change is a one-way door (hard to reverse: destructive migrations, deleted data, published releases, public contracts) or a two-way door (cheap to roll back), and its blast radius: who or what could break if it is wrong.
- **Review:** the review outcome on the final head.
- **Model and harness:** end with the verified model and harness that produced the change.

Keep private details out: local paths, hostnames, private links, credentials, transcripts, and customer data. When updating an open PR, edit its description rather than posting a comment, unless the user asked for a comment.
