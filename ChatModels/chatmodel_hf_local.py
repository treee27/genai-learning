from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from transformers import pipeline
from dotenv import load_dotenv
load_dotenv()

pipeline = pipeline(
    "text-generation",
    model="facebook/opt-125m",
    max_new_tokens=100
)

llm=HuggingFacePipeline(pipeline=pipeline)

result = llm.invoke("Write a 10 line poem about the ocean.")
print(result)

