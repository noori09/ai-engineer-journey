"""
Day 10 — Experiment 1: Comparing the three Claude models.

Same prompt, three different models. We'll observe the
quality/cost tradeoff with our own eyes.
"""

import os
import time
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

# A prompt that benefits from real thinking — not just trivia.
# It tests reasoning, structure, and depth.
PROMPT = (
    "I'm a frontend engineer learning AI engineering. "
    "In 3 short bullet points, explain why output tokens cost more than input tokens "
    "in LLM APIs. Be specific about what's happening under the hood."
)

MODELS = [
    ("Haiku 4.5", "claude-haiku-4-5-20251001"),
    ("Sonnet 4.6", "claude-sonnet-4-6"),
    ("Opus 4.7",   "claude-opus-4-7"),
]

for name, model_id in MODELS:
    print("=" * 70)
    print(f"MODEL: {name}  ({model_id})")
    print("=" * 70)

    start = time.time()
    response = client.messages.create(
        model=model_id,
        max_tokens=400,
        messages=[{"role": "user", "content": PROMPT}],
    )
    elapsed = time.time() - start

    print(response.content[0].text)
    print()
    print(f"--- input tokens: {response.usage.input_tokens}")
    print(f"--- output tokens: {response.usage.output_tokens}")
    print(f"--- time taken: {elapsed:.2f} seconds")
    print()
    


# ============================================================
# Experiment 2: max_tokens — the cliff
# ============================================================
print()
print("=" * 70)
print("EXPERIMENT 2: max_tokens — what happens when we cut Claude off")
print("=" * 70)

# A prompt that NATURALLY wants to produce a long answer.
LONG_PROMPT = "Tell me a short bedtime story about a brave little frog."

# We'll ask the SAME prompt with three different max_tokens ceilings.
CEILINGS = [30, 100, 500]

for ceiling in CEILINGS:
    print()
    print(f"--- max_tokens = {ceiling} ---")

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",  # Haiku is fine — and cheap — for this
        max_tokens=ceiling,
        messages=[{"role": "user", "content": LONG_PROMPT}],
    )

    print(response.content[0].text)
    print()
    print(f"   stop_reason: {response.stop_reason}")
    print(f"   output tokens: {response.usage.output_tokens}")
    
# ============================================================
# Experiment 3: temperature — the randomness dial
# ============================================================
print()
print("=" * 70)
print("EXPERIMENT 3: temperature — same prompt, different randomness")
print("=" * 70)

# A prompt that has MANY equally-valid answers.
# This is the kind of prompt where temperature matters most.
CREATIVE_PROMPT = "Give me one creative name for a coffee shop. Just the name, nothing else."

# Run the same prompt 5 times at temperature 0, then 5 times at temperature 1.
for temp in [0.0, 1.0]:
    print()
    print(f"--- temperature = {temp} ---")
    for i in range(5):
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=50,
            temperature=temp,
            messages=[{"role": "user", "content": CREATIVE_PROMPT}],
        )
        print(f"  Run {i+1}: {response.content[0].text}")