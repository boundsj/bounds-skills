# Confidence rules

Historical evidence is fragmentary, biased, and sometimes contradictory. These rules keep the answer from turning guesses into facts the user will act on.

## Tiers

Every claim sits in one tier, which sets its section and phrasing.

- **Direct:** an author wrote the reason down: a commit or review comment, a ticket, a code comment, a design document, a chat message. State it plainly and cite it: "This exists because X [source]."
- **Supported:** several indirect items converge, such as a "perf" label, a review that benchmarks the hot path, and tests that all use very large inputs. Cite each item: "The evidence points strongly to X: A, B, C."
- **Inferred:** a reasonable reading nothing states. Show the chain and hedge it: "Given A and B, C seems likely because D."
- **Speculative:** plausible, but other explanations fit as well. "One possibility is X; we found no direct evidence." Usually belongs under alternatives.
- **Unknown:** you looked and could not find out. Name what you searched, the queries, and what came back.

Direct and supported claims go under Found. Inferred claims go under Inferred. Speculative claims go under Alternatives. Unknowns go under Unknown.

## Phrasing

Words that claim intent or outcome ("because", "was designed to", "fixes", "the team decided") need an adjacent citation. Hedges ("appears to", "likely", "is consistent with") mark interpretation. Avoid "obviously", "clearly", "of course", and "just"; they usually cover a gap.

## Traps

- **Code as its own motive.** Code shows mechanics. "The author chose a functional style" is an observation, not evidence of intent.
- **Rationalizing.** Do not retrofit a clean reason onto messy history or assume a repeated pattern was deliberate rather than copied.
- **Recency.** The latest commit is rarely the whole story. Trace earlier decisions.
- **Confirming the user's guess.** Test it like any other candidate.
- **Silent substitution.** Evidence about a neighboring feature does not answer the question about this one.
- **Absence as evidence.** "Nobody mentioned security" does not mean security was not a concern.

## Contradictions and gaps

Show both sides of a contradiction with citations; do not pick the tidier story. Both may be true, such as a ticket giving the business reason and a commit giving the author's framing.

An honest gap is useful: it tells the user to ask a person or stop digging. An empty Unknown section is suspicious; historical investigations almost always have gaps.

## Before returning

Check that every Found claim has a citation, every phrase matches its tier, contradictions are visible, the embedded hypothesis was tested, no claim cites code for its own intent, and the overall tone is no more confident than the evidence.
