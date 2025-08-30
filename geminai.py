import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyBgy9UPfuSmIQlM041iD4rt_hhggaGIQCw")

# Load a Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Start a chat session
chat = model.start_chat(history=[])

print("🤖 Gemini Chatbot (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chat ended. Goodbye!")
        break

    # Send user input to Gemini
    response = chat.send_message(user_input)
    
    # Print Gemini's response
    print("Gemini:", response.text)
