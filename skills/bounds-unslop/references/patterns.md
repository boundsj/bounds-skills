# Patterns

Candidates to fix, not mechanical rules. Each fix must keep the meaning, and the destination's own style wins.

## Content

- **Empty -ing tails.** "...highlighting the importance of X", "ensuring Y". Delete, or state the actual consequence.
- **Vague attribution.** "Experts say", "some argue". Name the source when supplied; otherwise flag the missing attribution without inventing or deleting a factual claim.
- **Says how it feels, not what it does.** "SQL you can read" becomes "`.toSQL()` returns the exact query sent". If a sentence could appear unchanged in another project's docs, it probably says nothing about this one.
- **Generic conclusions.** "The future looks bright." Replace with the specific plan or fact, or cut.

## Words

- **Inflated vocabulary.** Delve, pivotal, crucial, robust, seamless, landscape, tapestry, testament, underscore, showcase, foster, leverage, utilize, facilitate. Use the plain word.
- **Fancy "is".** "Serves as", "stands as", "boasts". Say "is" or "has".
- **Abstract metaphor nouns.** Substrate, vector, surface, north star, flywheel, scaffolding, paradigm. Use the concrete term.
- **Synonym cycling.** One concept, one name, repeated.
- **Adverb propping a weak verb.** "Significantly improves" becomes the measured change; "runs quickly" becomes the number.

## Sentences

- **"Not just X, but Y".** State Y.
- **Forced threes.** Use the natural count.
- **False ranges.** "From X to Y" where X and Y are not on a scale. List the items.
- **Passive voice hiding the actor.** "Requests are validated" becomes "the gateway validates requests", unless the actor is unknown or irrelevant.
- **Dense sentences.** If the reader must backtrack, split it.
- **Over-compression.** Dropped articles, arrows, and private abbreviations. "Parser rejects bad date → exit 2" becomes "The parser rejects a bad date and exits with code 2."
- **Stacked hedges.** "Could potentially possibly" becomes the one hedge the evidence supports. Do not remove a hedge the evidence requires.
- **Mannered prose.** Aphorisms, dramatic fragments, personified code. Say it literally.

## Formatting

- **Inline-header lists** whose bold label restates the line ("**Performance:** Performance improved"). Use prose. A bold lead-in followed by new detail is fine.
- **Bold, emoji, and dash overuse.** Reduce to what helps scanning. Follow the destination's style for headings, quotes, and dashes.

## Chat residue

- "Great question", "Certainly!", "I hope this helps", "Let me know if...". Remove.
- Filler: "in order to" becomes "to", "due to the fact that" becomes "because", "it is important to note that" is deleted.
