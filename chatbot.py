def get_response(user_input):
    user_input = user_input.lower()
    
    responses = {
        'hi': ['Hello!', 'Hi there!', 'Greetings!'],
        'how are you': ['I’m doing well, thank you!', 'I’m good, how about you?', 'I’m great! How can I assist you?'],
        'bye': ['Goodbye!', 'See you later!', 'Take care!'],
    }
    
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return "Sorry, I don't understand that."

def chat():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
