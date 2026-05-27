import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
system_prompts = ["You are a friendly elementary school teacher. Explain things in simple terms a 10-year-old would understand. Use short sentences.",
"You are a curt, no-nonsense engineer. Answer in 2 sentences maximum. No fluff, no analogies, no pleasantries.",
"You are a Shakespearean poet. Respond only in rhyming couplets in iambic pentameter, with archaic English (thee, thou, doth)."]

for prompt in system_prompts:
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=500,                  
        temperature=0.7,                
        system=prompt,
        messages=[{"role": "user", "content": "Why is the sky blue?"}],
    )
    
    print("=" * 70)
    print(f"SYSTEM PROMPT: {prompt}")
    print("=" * 70)
    print(response.content[0].text)
    print()
    print(f"   stop_reason:   {response.stop_reason}")
    print(f"   output tokens: {response.usage.output_tokens}")
    print()