from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import getpass
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

chat_history = [] # using a list to store messages

# setting an intial system messgae
SystemMessage = SystemMessage(content = "You are a helpful AI assistant.")
chat_history.append(SystemMessage)

#chat loop
while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("Exiting the chat.")
        break
    chat_history.append(HumanMessage(content=query))#adds user message
    
    # get ai response using history
    reusult = model.invoke(chat_history)
    response = reusult.content
    chat_history.append(AIMessage(content=response))#adds ai response
    
    print(f"AI: {response}")  # prints the AI response
    
    
print("\n--- Chat History ---")
print(chat_history)  # prints the chat history for reference





