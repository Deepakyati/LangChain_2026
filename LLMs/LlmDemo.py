from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv() #API keys gets loaded, from env file to current file

llm=OpenAI(model='gpt-3.5-turbo-instruct')

llm.invoke('what is the capital of India')