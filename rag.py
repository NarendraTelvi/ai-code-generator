import json

from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

DB_PATH = "chroma_db"

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def create_db():

    with open(
        "data/code_examples.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    texts = []

    for item in data:

        text = f"""
        Requirement:
        {item['requirement']}

        Code:
        {item['code']}
        """

        texts.append(text)

    Chroma.from_texts(
        texts=texts,
        embedding=embedding,
        persist_directory=DB_PATH
    )

    print("Database Created")


def retrieve_context(query):

    db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding
    )

    docs = db.similarity_search(
        query,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context