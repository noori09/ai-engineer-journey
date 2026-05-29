import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()

print("Welcome! Chat with Claude. Type quit to exit")

messages = []

while True:
    user_input = input("You : ")
    if user_input.strip().lower() == "quit":
        break
    messages.append({"role": "user", "content": user_input})
    response = client.messages.create(
        model="claude-haiku-4-5", 
        max_tokens=500, 
        messages=messages
    )
    reply = response.content[0].text
    print(f"Claude : {reply}")
    messages.append({"role": "assistant", "content": reply})
