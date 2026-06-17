import streamlit as st

from components.sidebar import admin_sidebar
from rag.vector_store import load_vector_store

st.set_page_config(
    page_title="Document Summaries",
    layout="wide"
)

admin_sidebar()

st.title(
    "📋 Document Summaries"
)

vector_data = load_vector_store()

if not vector_data:

    st.warning(
        "No documents available."
    )

    st.stop()

_, chunks = vector_data

for i, chunk in enumerate(
    chunks[:20],
    start=1
):

    with st.expander(
        f"Chunk {i}"
    ):

        st.write(
            chunk[:1000]
        )