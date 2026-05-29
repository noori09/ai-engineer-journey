# Day 13 — Part 1: Cost instrumentation

**Date:** May 30, 2026

## What I built
Added per-turn token logging and running cost total to my chat app.
Created `calculate_cost(input_tokens, output_tokens)` helper using Haiku pricing.

## The headline observation
By Turn 5, input was 337 tokens vs Turn 1's 14 tokens.
Same length user message — but Turn 5 paid ~24x more for input than Turn 1.
**Memory = the user pays N times for the same words.**

## Rules I'm taking forward
- Always log `response.usage` in production. It's free data and you need it.
- Cost = (input_tokens × in_rate + output_tokens × out_rate) / 1_000_000
- Conversation cost is dominated by input growth, not output growth.
  Output stays steady per turn; input balloons.

## What's next
Day 13 Part 2: Error handling with try/except.