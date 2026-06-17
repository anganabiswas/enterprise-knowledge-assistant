from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

FAISS_PATH = "vector_db/faiss_index.bin"
CHUNKS_PATH = "vector_db/chunks.pkl"


def create_vector_store(chunks):

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(
        np.array(embeddings)
    )

    os.makedirs(
        "vector_db",
        exist_ok=True
    )

    faiss.write_index(
        index,
        FAISS_PATH
    )

    with open(
        CHUNKS_PATH,
        "wb"
    ) as f:

        pickle.dump(
            chunks,
            f
        )

    return index


def load_vector_store():

    if (
        not os.path.exists(FAISS_PATH)
        or
        not os.path.exists(CHUNKS_PATH)
    ):
        return None

    index = faiss.read_index(
        FAISS_PATH
    )

    with open(
        CHUNKS_PATH,
        "rb"
    ) as f:

        chunks = pickle.load(f)

    return index, chunks


def add_documents(new_chunks):

    existing_data = load_vector_store()

    if existing_data:

        _, old_chunks = existing_data

        all_chunks = (
            old_chunks +
            new_chunks
        )

    else:

        all_chunks = new_chunks

    return create_vector_store(
        all_chunks
    )