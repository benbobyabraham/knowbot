import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

# Check what we have
print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')[:20] if os.getenv('OPENAI_API_KEY') else 'NOT SET'}...")
print(f"OPENAI_API_KEY_EMBED: {os.getenv('OPENAI_API_KEY_EMBED')[:20] if os.getenv('OPENAI_API_KEY_EMBED') else 'NOT SET'}...")
print(f"OPENAI_API_BASE: {os.getenv('OPENAI_API_BASE', 'NOT SET')}")

# Use embed key since that's what works
api_key = os.getenv("OPENAI_API_KEY_EMBED")
if not api_key:
    print("ERROR: OPENAI_API_KEY_EMBED is not set!")
    exit(1)

client = OpenAI(
    api_key=api_key,
    base_url="https://api.openai.com/v1",
)

print("\nTesting OpenAI API...")
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Reply with OK"}]
)
print(f"✅ Response: {r.choices[0].message.content}")
