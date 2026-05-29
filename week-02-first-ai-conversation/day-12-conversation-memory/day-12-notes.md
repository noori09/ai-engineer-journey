# Day 12 — Conversation Memory

**Date:** May 29 and 30, 2026
**Goal:** Conversation Memory:

## The core idea

Every Claude API call is stateless — Anthropic stores nothing between calls.
"Memory" isn't a Claude feature. It's a list I maintain in my code, sent in full
on every API call. Claude doesn't remember me across calls; I remind it every time
by sending the whole conversation history.

This means:
- The "memory" lives in my code (the `messages` list), not in Claude
- Every turn re-sends the full history → conversation cost grows quadratically
- Eventually long conversations hit the context window ceiling (200K for Haiku)
- Real production apps use sliding windows, summarization, or external memory
  stores to manage this

## Experiment 1 - 
`memory_demo.py` — I had added two turns, First turn was role user and its content and after my first turn i appended claudes reply where role was assistant. In this way i have given memory to claude so that it remembers what i have said to claude in my previous message.

**Observations:**
- We have to provide memory to claude with the help of role assistant.
- If we dont provide role assistant in message, claude wont remember anything from prev message and  every message will act as a new conversation.


**My takeaway:** If i want claude to remember my context i will have to append claude's reply in the next message

## Experiment 2:
`memory_demo_broken.py` — I had added two turns, First turn was role user and its content and after my first turn i reset my message to check what happens next.

**Observations:**
- For first turn it replied me correctly
- For the second turn as we had cleared messages after first so again claude doesnot know about prev context.


**Key rule:** always append claudes reply in role assistant, but whenever we are asking any new qs the last object will always be role user and its always alternate like role -> user -> assistant -> user.
If we provide 2 role users one after the other claude will not be able to provide ans correctly.
so always remember the end object should always be role user


## Experiment 3: 
`chat.py` — I have created one chatbot where i can ask multiple question until user quits

**Observations:**
- user_input should not be in {}
- user input can be stripped and lowered before comparing with quit
- no need for else and continue we can directly write our code

## Rules I'm taking forward

- Append claude's reply whenever needed 
- user input should not be in {} to avoid error.
- print full messages list at the end
- Conversation cost grows quadratically. Turn N's input includes turns 1..N-1.
  A 50-turn chat is ~1250x the cost of a single turn, not 50x.
  Plan for this from the start — sliding window, summarization, or external memory.

## What's next

Day 13: Error handling and Costs