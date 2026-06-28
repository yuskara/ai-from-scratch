from ollama_client import ask_ai


def start_chat():

    print("AI Chat Started")
    print("Type 'exit' to quit\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        answer = ask_ai(user_input)

        print("\nAI:", answer)
        print()


if __name__ == "__main__":
    start_chat()