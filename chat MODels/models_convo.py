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


messages = [
    SystemMessage("You are a content creator."),
    HumanMessage("Write a short story about a robot learning to love."),
    
]
output = model.invoke(messages)
print (output.content)

