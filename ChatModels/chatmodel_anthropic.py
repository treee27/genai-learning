from langchain_anthropic import chatAnthropic

from dotenv import load_dotenv
load_dotenv()

chat_model = chatAnthropic(model="claude-v1", temperature=0.7,max_completion_tokens=10)
result = chat_model.invoke("Write a poem about the ocean.")

print(result.content)
