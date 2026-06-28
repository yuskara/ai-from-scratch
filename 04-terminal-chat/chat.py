from colorama import Fore, Style, init
from ollama_client import chat

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