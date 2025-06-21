def chatbot():
    print("Chatbot: Hello! Let's chat. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi there!")
        elif user_input == "how are you":
            print("Chatbot: I'm doing great, thanks! How about you?")
        elif user_input == "what's your name":
            print("Chatbot: I'm ChatBot 1.0!")
        elif user_input == "what can you do":
            print("Chatbot: I can have a simple chat with you.")
        elif user_input == "tell me a joke":
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
        elif user_input == "thank you":
            print("Chatbot: You're welcome!")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that yet.")

# Run the chatbot
chatbot()