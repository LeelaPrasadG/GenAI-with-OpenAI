if __name__ == "__main__":
    import sys
    from GenAI_Chat import main

    # Check if the script is being run directly
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        main()
    else:
        print("Please run this script with 'run' argument to start the chat.")

def main():
    print("Welcome to the GenAI Chat!")
    # Here you would implement the chat functionality
    # For example, initializing a chat session, processing user input, etc.
    # This is a placeholder for the actual chat logic.
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        else:
            print(f"GenAI: You said '{user_input}'")  # Placeholder response