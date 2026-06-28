import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:14b"

def chat(messages):
    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    data = response.json()
    return data["message"]["content"]