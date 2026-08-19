from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()
chat_model = ChatGoogleGenerativeAI(model="gemini-3.6-flash",temperature=0)
result = chat_model.invoke("Write a 5 line poem about the ocean.")
print(result.content[0]["text"])
