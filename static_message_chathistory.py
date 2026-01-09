from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_BASE = os.getenv("OPENROUTER_API_BASE")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenAI(
    model="allenai/olmo-3.1-32b-think:free",
    openai_api_key = OPENROUTER_API_KEY,
    openai_api_base = OPENROUTER_API_BASE
)

#Single message : Static message with Chat history
#Single turn stand alone queries
chat_history = []
chat = True
while(chat is True):
    print("Enter your prompt: ")
    user_prompt = input()
    chat_history.append(user_prompt)
    answer = model.invoke(chat_history)
    print("Chatbot: ",answer.content)
    chat_history.append(answer.content)
    chat_continuation = input("Wanna continue chat (y/n)")
    if chat_continuation == "n":
        chat = False

#Chat History
print(chat_history)