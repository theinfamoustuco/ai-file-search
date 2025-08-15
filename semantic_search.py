from sentence_transformers import SentenceTransformer
import numpy as np
import os

# Load the embedding model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def preprocess_filename(file_path):
    file_name = os.path.basename(file_path)
    name = os.path.splitext(file_name)[0]
    name = name.replace("_", " ").replace("-", " ")
    return name.lower()

def build_embeddings(files):
    processed_files = [preprocess_filename(f) for f in files]
    embeddings = model.encode(processed_files, convert_to_numpy=True)
    return processed_files, embeddings

def semantic_search(query, files, top_k=10):
    if not files:
        return [], []

    processed_files, embeddings = build_embeddings(files)
    query_processed = query.lower()
    query_emb = model.encode([query_processed], convert_to_numpy=True)[0]

    similarities = np.dot(embeddings, query_emb) / (
        np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_emb)
    )

    top_indices = similarities.argsort()[::-1][:top_k]
    return [files[i] for i in top_indices], similarities[top_indices]
