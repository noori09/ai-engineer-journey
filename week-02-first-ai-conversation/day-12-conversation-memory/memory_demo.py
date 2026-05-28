import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()

messages = []
# --- Turn 1 ---

messages.append({"role":"user","content":"My name is Noori. Remember this"})

response = client.messages.create(
    model= "claude-haiku-4-5",
    max_tokens = 200,
    messages= messages
)

reply = response.content[0].text
print(f"Claude (turn 1): {reply}")

messages.append({"role": "assistant", "content": reply})

# --- Turn 2 ---
messages.append({"role": "user", "content": "What's my name?"})

response = client.messages.create(
    model= "claude-haiku-4-5",
    max_tokens = 200,
    messages= messages
)

reply = response.content[0].text
print(f"Claude (turn 2): {reply}")

messages.append({"role": "assistant", "content": reply})   

# --- Look at the structure ---
print()
print("Full messages list:")
print(messages)