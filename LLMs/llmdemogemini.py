from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv() #API keys gets loaded, from env file to current file

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

result=llm.invoke('what is the capital of India')

print(result)

