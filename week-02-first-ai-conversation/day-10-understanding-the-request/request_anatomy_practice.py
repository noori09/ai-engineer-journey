import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()

# Experimemt 1 : Comparing 3 diff models

# models = ["claude-haiku-4-5-20251001",
#     "claude-sonnet-4-6",
#     "claude-opus-4-7"]

# for model in models:
#     response = client.messages.create(
#         model= model,
#         max_tokens=1024,
#         messages = [{"role":"user","content":"I am a react developer with 7 years of experience.now i want to switch my career in ai engineering.Suggest some ways in which i can plan everything."}]
#     )
#     print("model",model)
#     print("="*70)
#     print("response -", response.content[0].text)
    
# Experiment 2 = Comparing diff token values with same prompt
   
# ceilings = [30,100,500]

# for ceiling in ceilings:
#     response = client.messages.create(
#         model="claude-haiku-4-5",
#         max_tokens = ceiling,
#         messages = [{"role":"user","content":"Tell me one bed time story"}]
#     )
    
#     print("="*70)
#     print(f"max_tokens:    {ceiling}")
#     print(f"stop_reason:   {response.stop_reason}")
#     print(f"output tokens: {response.usage.output_tokens}")
#     print(f"response:  {response.content[0].text}")
   
   
# Experiment 3 = Testing diff temperature values 

temperatures = [0.0, 1.0]  

for temperature in temperatures:
    print(f"\n--- temperature = {temperature} ---")
    for i in range(5):
        response = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=50,               
            temperature=temperature,
            messages=[{
                "role": "user",
                "content": "Give me one creative name for a coffee shop. Just the name, nothing else."
            }],
        )
        print(f"  Run {i+1}: {response.content[0].text}")
    