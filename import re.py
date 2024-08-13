import re

# Define a dictionary of patterns and responses
rules = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! How can I assist you?",
    "how are you": "I'm just a bot, but I'm here to help you!",
    "what is your name": "I'm ChatBot, your virtual assistant.",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! Happy to help.",
    "help": "Sure, I'm here to help! What do you need assistance with?",
    "weather": "I don't have real-time weather information, but you can check online for the latest updates."
}

# Function to find the appropriate response based on user input
def find_response(user_input):
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "I'm not sure how to respond to that. Can you please rephrase?"

# Main chatbot loop
def chat():
    print("ChatBot: Hello! I'm your virtual assistant. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "bye":
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = find_response(user_input)
        print(f"ChatBot: {response}")

# Start the chatbot
chat()