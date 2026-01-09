from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_BASE = os.getenv("OPENROUTER_API_BASE")

model = ChatOpenAI(
    model="allenai/olmo-3.1-32b-think:free",
    openai_api_key = OPENROUTER_API_KEY,
    openai_api_base = OPENROUTER_API_BASE
)

#Single message -> static message
#Static Message -> Single turn stand alone queries
chat = True
while(chat is True):
    print("Enter your prompt: ")
    user_prompt = input()
    answer = model.invoke(user_prompt)
    print("Chatbot: ",answer.content)
    print("Do you want to continue (yes/no): ")
    chat_continuation = input()
    if chat_continuation == "n":
        chat = False
    
#Static message -> stand alone queries with chat history
