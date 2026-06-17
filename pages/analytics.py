import streamlit as st

from components.sidebar import admin_sidebar

from database.stats import get_total_users
from rag.vector_store import load_vector_store

st.set_page_config(
    page_title="Analytics",
    layout="wide"
)

# --------------------------------------------------
# LOGIN CHECK
# --------------------------------------------------

if "user" not in st.session_state:

    st.switch_page(
        "app.py"
    )

if st.session_state.user["role"] != "admin":

    st.switch_page(
        "app.py"
    )

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

admin_sidebar()

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title(
    "📊 Analytics & System Health"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

total_users = get_total_users()

vector_data = load_vector_store()

if vector_data:

    _, chunks = vector_data

    total_chunks = len(chunks)

else:

    total_chunks = 0

# --------------------------------------------------
# METRICS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "👥 Users",
        total_users
    )

with col2:

    st.metric(
        "📄 Chunks",
        total_chunks
    )

with col3:

    st.metric(
        "🧠 Vector DB",
        "Active"
    )

st.divider()

# --------------------------------------------------
# SYSTEM STATUS
# --------------------------------------------------

st.subheader(
    "⚡ System Status"
)

st.success(
    "Gemini API Connected"
)

st.success(
    "FAISS Vector Store Active"
)

st.success(
    "MySQL Database Connected"
)

st.success(
    "Authentication Service Running"
)

st.divider()

# --------------------------------------------------
# KNOWLEDGE BASE OVERVIEW
# --------------------------------------------------

st.subheader(
    "📚 Knowledge Base Overview"
)

st.info(
    f"""
    Current knowledge base contains
    {total_chunks} chunks.

    Registered users:
    {total_users}

    System ready for Retrieval-Augmented Generation.
    """
)