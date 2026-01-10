import torch
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

while True:
    user_input=input("Enter your prompt (or type 'exit' to quit): ")
    if user_input.lower()=='exit':
        break
    result=model.invoke(user_input)
    print("AI: ",result.content)