# ----------- 1. Install dependencies -----------
# pip install openai faiss-cpu langchain-community langchain

import os
from openai import OpenAI
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Set your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ----------- 2. Your documents -----------
documents = [
    "RAG stands for Retrieval Augmented Generation.",
    "It works by retrieving relevant text chunks and passing them to a language model.",
    "FAISS is a vector store used to perform similarity search efficiently."
]

# ----------- 3. Split text into chunks -----------
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
docs = splitter.create_documents(documents)

# ----------- 4. Create embeddings + vector store -----------
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = FAISS.from_documents(docs, embedding_model)

# ----------- 5. RAG retrieval function -----------
def rag_query(question: str):
    # Retrieve similar chunks
    results = vectorstore.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in results])

    # Create prompt for the LLM
    prompt = f"""
You are a helpful assistant. Use the context below to answer the question.

Context:
{context}

Question: {question}
Answer:
    """

    # LLM call
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()

# ----------- 6. Example query -----------
user_question = "What is RAG?"
answer = rag_query(user_question)

print("User question:", user_question)
print("Answer:", answer)
