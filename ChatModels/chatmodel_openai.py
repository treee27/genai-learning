from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

chat_model = ChatOpenAI(model="gpt-4", temperature=0.7,max_completion_tokens=10)
result = chat_model.invoke("Write a poem about the ocean.") 

print(result.content)





