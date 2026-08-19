from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro-0813",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Write a poem about the ocean.")

print(result.content)
