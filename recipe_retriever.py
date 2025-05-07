def embed_query(text_query):
    """
    Embed a user text query (ingredients list) using the same embedding model.
    """
    return embedding_model.encode([text_query])

def search_recipes(ingredient_query, top_k=5):
    """
    Given an ingredient list (string), return top_k matching recipes.
    """
    # Embed the query
    query_embedding = embed_query(ingredient_query)

    # Search collection
    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=top_k,
        include=["documents"]
    )

    # Return matched recipe texts
    return results["documents"][0]