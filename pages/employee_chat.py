import streamlit as st

from components.sidebar import (
    admin_sidebar,
    employee_sidebar
)

from rag.vector_store import load_vector_store
from rag.retriever import retrieve_chunks
from rag.gemini_handler import generate_answer

from database.chat_history import save_chat


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Enterprise AI Assistant",
    layout="wide"
)

# --------------------------------------------------
# LOGIN CHECK
# --------------------------------------------------

if "user" not in st.session_state:

    st.switch_page(
        "app.py"
    )

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

if st.session_state.user["role"] == "admin":

    admin_sidebar()

else:

    employee_sidebar()

# --------------------------------------------------
# PAGE TITLE
# --------------------------------------------------

st.title(
    "🤖 Enterprise AI Assistant"
)

st.info(
    "Ask questions from uploaded company documents."
)

# --------------------------------------------------
# LOAD VECTOR STORE
# --------------------------------------------------

vector_data = load_vector_store()

if vector_data:

    index, chunks = vector_data

else:

    index = None
    chunks = []

# --------------------------------------------------
# QUESTION INPUT
# --------------------------------------------------

question = st.text_input(
    "Ask a Question"
)

# --------------------------------------------------
# ASK QUESTION
# --------------------------------------------------

if st.button(
    "🚀 Ask Question",
    use_container_width=True
):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    elif index is None:

        st.error(
            "Knowledge Base not loaded."
        )

    else:

        with st.spinner(
            "Searching documents..."
        ):

            retrieved_chunks = retrieve_chunks(
                question,
                chunks,
                index
            )

            context = "\n\n".join(
                retrieved_chunks
            )

            answer = generate_answer(
                context,
                question
            )

            save_chat(
                st.session_state.user["id"],
                question,
                answer
            )

        st.success(
            answer
        )

        st.subheader(
            "📄 Sources Used"
        )

        for i, chunk in enumerate(
            retrieved_chunks,
            start=1
        ):

            with st.expander(
                f"Source {i}"
            ):

                st.write(
                    chunk
                )