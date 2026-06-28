import requests
import json

url = "http://localhost:11434/api/generate"

prompt = input("You: ")

response = requests.post(
    url,
    json={
        "model": "qwen3:14b",
        "prompt": prompt,
        "stream": True
    },
    stream=True
)

print("\nAI: ", end="", flush=True)

for line in response.iter_lines():
    if line:
        data = json.loads(line)

        print(data["response"], end="", flush=True)

        if data.get("done"):
            break

print()