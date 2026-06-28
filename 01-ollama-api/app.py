import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen3:14b",
    "prompt": "Explain what Ollama is in one paragraph.",
    "stream": False,
}

try:
    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    data = response.json()

    print("\n=== AI Response ===\n")
    print(data["response"])

except requests.exceptions.RequestException as e:
    print(f"Error connecting to Ollama: {e}")

except KeyError:
    print("Unexpected response format from Ollama.")