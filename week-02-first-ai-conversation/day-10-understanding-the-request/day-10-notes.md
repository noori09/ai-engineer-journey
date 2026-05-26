# Day 10 — Understanding the Request

**Date:** May 27, 2026
**Goal:** Understand the three core parameters of `client.messages.create()`:
`model`, `max_tokens`, `temperature`.

## What I built

`request_anatomy.py` — three experiments, one script.

## Experiment 1: Comparing models

Ran the same prompt through Haiku 4.5, Sonnet 4.6, and Opus 4.7.

**Observations:**
- All three got the technical answer correct.
- Output length grew with model size: Haiku 207 tokens, Sonnet 279, Opus 334.
- Latency was roughly: Haiku 4s, Sonnet 8s, Opus 7s (single-sample, not reliable).
- Total cost for all three calls: ~1.4 US cents (~₹1.20).
- Opus alone cost 8x what Haiku cost — bigger models also write more, compounding the price gap.

**My takeaway:** i will choose haiku when i need quick chat replies and anything where i just need an answer
sonnet is default and will use it whenever writing, coding or in any customer facing app 
opus i will use it when the task is hard reasoning like when i need complex code refactors,multi-step planning

"Within a single app, route by task. Haiku for routing/classification/extraction. Sonnet by default for user-facing generation. Opus only for the specific calls where Sonnet visibly fails."

## Experiment 2: max_tokens

Ran the same "bedtime story" prompt at `max_tokens` = 30, 100, 500.

**Observations:**
- At 30 tokens: cut off mid-sentence ("...at the edge of a quiet pond"). No grace.
- At 100 tokens: story was mid-narrative — looked plausible but was incomplete.
  Dangerous gray zone.
- At 500 tokens: Claude finished naturally at 271 tokens. `stop_reason` was `end_turn`.

**Key rule:** `max_tokens` is a ceiling, not a target. Set it generously
as a cost safety valve, but use the prompt itself (not the ceiling) to control length.

**Production rule:** always log `stop_reason`. If it's `"max_tokens"`,
the response was truncated and should be treated as broken.

## Experiment 3: temperature

Same prompt ("creative coffee shop name") 5 times at temp 0, then 5 at temp 1.

**Observations:**
- Temp 0: "Brew & Bloom" — 5 out of 5 times. Pure determinism.
- Temp 1: 4 distinct names ("Grounds for Thought," "Brew Awakening,"
  "Brew & Bloom" ×2, "Brew & Reverie"). Three still started with "Brew" —
  the underlying probability distribution still showed through.

**My takeaway:** temperature actually computes the probability distribution over thousands of possible next tokens
temp = 0 -> determinitstic-ish same prompt-> same ans mostly
temp = 1.0 -> creative,varied
temp b/w 0.3, 0.5, 0.7 -> mostly deterministic but with some variety
above 1 -> wont go as anthropic allows up to 1.0

"Temperature trades reliability for variance. Default to 0 for anything where correctness matters (extraction, classification, JSON, math, factual Q&A). Default to 0.7–1.0 only when variety is the explicit goal (brainstorming, creative writing, multiple suggestions). The SDK defaults to temperature=1.0 if you don't set it. Most production code wants something lower. Always set temperature explicitly — don't inherit the default."

## Rules I'm taking forward

- Default to Haiku. Climb to Sonnet/Opus only when Haiku visibly fails.
- Output is 5x the cost of input. Feed Claude context, ask for concise output.
- `max_tokens` should be a safety ceiling, not a length target. Always log `stop_reason`.
- Default to temperature 0 for anything where correctness > variety.
  Temperature 1 only when variety is the explicit goal.
- The SDK default temperature is 1.0 — most production code overrides it.

## What's next

Day 11: System prompts — giving Claude a persona, ground rules, and context.