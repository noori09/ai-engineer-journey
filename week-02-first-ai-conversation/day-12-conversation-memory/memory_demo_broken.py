import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()

messages = []

# ---- Turn 1 ----
messages.append({"role":"user","content":"My name is Noori"})

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens = 200,
    messages = messages
)
reply = response.content[0].text
print("=" * 70)
print(f"Response : {reply}")
print(f"messages : {messages}")

messages = []

# ---- Turn 2 ------

messages.append({"role":"user","content":"What is my Name?"})

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens = 200,
    messages = messages
)
reply = response.content[0].text
print("=" * 70)
print(f"Response : {reply}")
print(f"messages : {messages}")
