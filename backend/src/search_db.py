from langchain_community.vectorstores import FAISS

from src.embeddings import get_embedding_model



def search_query(query):

    embeddings = get_embedding_model()


    db = FAISS.load_local(
        "vector_store/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )


    results = db.similarity_search(
        query,
        k=3
    )


    return results