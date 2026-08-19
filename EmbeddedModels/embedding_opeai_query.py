from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1536)

result=embeddings.embed_query("Write a poem about the ocean.")

print(result)