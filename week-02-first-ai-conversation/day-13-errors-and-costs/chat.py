import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Haiku 4.5 pricing ( per million tokens )
HAIKU_INPUT_PER_MTOK = 1.0   # 1$ per million tokens
HAIKU_OUTPUT_PER_MTOK = 5.0  # 5$ per million tokens

# Rough USD to INR conversion
USD_TO_INR = 84.0


load_dotenv()

client = Anthropic()

print("Welcome! Chat with Claude. Type quit to exit")

messages = []
total_cost_inr = 0.0

def calculate_cost(input_tokens,output_tokens):
    """ Return cost in INR for one claude API call"""
    input_cost_usd = (input_tokens / 1_000_000) * HAIKU_INPUT_PER_MTOK
    output_cost_usd = (output_tokens / 1_000_000) * HAIKU_OUTPUT_PER_MTOK
    total_usd = input_cost_usd + output_cost_usd
    return total_usd * USD_TO_INR

while True:
    user_input = input("You : ")
    if user_input.strip().lower() == "quit":
        print(f"\nTotal conversation cost: ₹{total_cost_inr:.4f}")
        break
    messages.append({"role": "user", "content": user_input})
    response = client.messages.create(
        model="claude-haiku-4-5", 
        max_tokens=500, 
        messages=messages
    )
    reply = response.content[0].text
    input_tokens = response.usage.input_tokens
    output_tokens = response.usage.output_tokens
    turn_cost = calculate_cost(input_tokens,output_tokens)
    total_cost_inr += turn_cost
    print(f"Claude : {reply}")
    print(f"   [tokens in/out: {input_tokens}/{output_tokens} | turn: ₹{turn_cost:.4f} | total: ₹{total_cost_inr:.4f}]")
    messages.append({"role": "assistant", "content": reply})
