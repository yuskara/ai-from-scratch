import importlib


class _FallbackFore:
    GREEN = ""
    CYAN = ""
    RED = ""


try:
    colorama = importlib.import_module("colorama")
    Fore = colorama.Fore
    init = colorama.init
except ModuleNotFoundError:
    Fore = _FallbackFore

    def init(*args, **kwargs):
        return None

try:
    from ollama_client import chat
except ModuleNotFoundError as exc:
    if exc.name == "requests":
        print("Missing dependency 'requests'. Install it with: python -m pip install -r requirements.txt")
        raise SystemExit(1)
    raise

init(autoreset=True)

history = []

print("=" * 40)
print(" Local AI Assistant")
print("=" * 40)
print("Type 'exit' to quit.\n")

while True:
    user_input = input(Fore.GREEN + "You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    if not user_input.strip():
        continue

    history.append({
        "role": "user",
        "content": user_input
    })

    try:
        answer = chat(history)

        print(Fore.CYAN + "\nAI:")
        print(answer)
        print()

        history.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        print(Fore.RED + f"Error: {e}")