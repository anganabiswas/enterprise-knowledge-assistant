from rag.document_loader import load_pdf
from rag.text_splitter import split_text
from rag.vector_store import create_vector_store
from rag.retriever import retrieve_chunks
from rag.gemini_handler import generate_answer

text = load_pdf("sample.pdf")

chunks = split_text(text)

index = create_vector_store(chunks)

question = "What certifications does this person have?"

retrieved_chunks = retrieve_chunks(
    question,
    chunks,
    index
)

context = "\n".join(retrieved_chunks)

answer = generate_answer(
    context,
    question
)

print("\nANSWER:\n")
print(answer)