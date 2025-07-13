import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I'm a simple chatbot created using Python and NLTK."]
    ],
    [
        r"how are you?",
        ["I'm just a bunch of code, but I'm functioning properly!"]
    ],
    [
        r"what can you do?",
        ["I can answer basic questions. Try asking me about my name or how I'm doing!"]
    ],
    [
        r"(.*) your creator?",
        ["I was created by a Python developer for a project."]
    ],
    [
        r"(bye|exit|quit)",
        ["Goodbye! Have a nice day."]
    ],
    [
        r"(.*)",
        ["Sorry, I don't understand that. Can you rephrase?"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chat
print("🤖 Welcome to the Chatbot. Type 'quit' to exit.")
chatbot.converse()
