import os
import streamlit as st

from components.sidebar import admin_sidebar

from rag.document_loader import load_pdf
from rag.text_splitter import split_text

from rag.vector_store import (
    add_documents,
    load_vector_store
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Upload Documents",
    layout="wide"
)

# --------------------------------------------------
# LOGIN CHECK
# --------------------------------------------------

if "user" not in st.session_state:

    st.switch_page("app.py")

if st.session_state.user["role"] != "admin":

    st.switch_page("app.py")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

admin_sidebar()

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📤 Upload Documents")

st.info(
    "Upload PDF documents to build the company knowledge base."
)

# --------------------------------------------------
# KB STATS
# --------------------------------------------------

vector_data = load_vector_store()

if vector_data:

    _, chunks = vector_data

    st.metric(
        "📄 Total Chunks",
        len(chunks)
    )

else:

    st.metric(
        "📄 Total Chunks",
        0
    )

st.divider()

# --------------------------------------------------
# PDF UPLOAD
# --------------------------------------------------

uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button(
    "🚀 Process Documents"
):

    if not uploaded_files:

        st.warning(
            "Please upload PDF files."
        )

    else:

        all_text = ""

        with st.spinner(
            "Processing documents..."
        ):

            for uploaded_file in uploaded_files:

                with open(
                    uploaded_file.name,
                    "wb"
                ) as f:

                    f.write(
                        uploaded_file.getbuffer()
                    )

                pdf_text = load_pdf(
                    uploaded_file.name
                )

                if pdf_text:

                    all_text += (
                        pdf_text + "\n"
                    )

            chunks = split_text(
                all_text
            )

            add_documents(
                chunks
            )

        st.success(
            f"✅ Added {len(chunks)} chunks successfully."
        )

st.divider()

# --------------------------------------------------
# CLEAR KB
# --------------------------------------------------

st.subheader(
    "🗑 Clear Knowledge Base"
)

if st.button(
    "Delete All Documents"
):

    if os.path.exists(
        "vector_db/faiss_index.bin"
    ):

        os.remove(
            "vector_db/faiss_index.bin"
        )

    if os.path.exists(
        "vector_db/chunks.pkl"
    ):

        os.remove(
            "vector_db/chunks.pkl"
        )

    st.success(
        "Knowledge Base Cleared."
    )

    st.rerun()