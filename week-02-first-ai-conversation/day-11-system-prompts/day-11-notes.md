# Day 11 — System Prompts

**Date:** May 28, 2026
**Goal:** Understand the system prompts :

## What I built

`system_prompts.py` — three system_prompts, one question.

## Experiment : Comparing diff system prompts output

Ran the same user prompt with 3 diff system prompts

**Observations:**
The same question — "Why is the sky blue?" — produced:

A 254-token kids' lesson with emoji, analogies, fun facts
A 51-token terse engineering reply that mentions Rayleigh by name and stops
A 103-token Shakespearean poem in rhyming couplets

Same client.messages.create(), same model, same temperature, same user message. The only thing that changed was a single string in the system parameter — and the output shape, length, vocabulary, tone, and structure all transformed.

system prompt = the role / job description I'm giving Claude before any conversation starts. User message = today's actual question. The system prompt is more 'authoritative' — Claude follows it harder than the user message.

**My takeaway:** 
A system prompt is a contract that shapes everything downstream. It's not "extra context for one message" — it's the role Claude plays for the entire conversation. Change the system prompt → change the AI. Same model, same code, different product.


## Rules I'm taking forward

- `system` is a top-level parameter — not inside `messages`. (Different from OpenAI.)
- Shape, don't fix. Tell Claude what you want from the start. "Be terse" works
  better than "don't be verbose."
- A precise short system prompt > a vague long one. 5 careful words can outperform 50 loose ones.

## API shape (for reference)

```python
response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=500,
    system="You are a ...",           # top-level parameter, plain string
    messages=[{"role": "user", "content": "..."}],
)
```

## What's next

Day 12: Conversation Memory