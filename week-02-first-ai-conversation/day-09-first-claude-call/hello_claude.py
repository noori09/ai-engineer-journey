import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables from .env file
load_dotenv()

# Initialize the Anthropic client
# It automatically reads ANTHROPIC_API_KEY from the environment
client = Anthropic()

# Send a message to Claude
response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "I'm transitioning from frontend to AI engineering. What's one thing I should focus on?"}
    ]
)

# Print Claude's reply
print("Claude says:")
print(response.content[0].text)