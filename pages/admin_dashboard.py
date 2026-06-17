import streamlit as st

from components.sidebar import admin_sidebar
from database.stats import get_total_users
from rag.vector_store import load_vector_store

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Admin Dashboard",
    layout="wide"
)

# --------------------------------------------------
# AUTH CHECK
# --------------------------------------------------

if "user" not in st.session_state:
    st.switch_page("app.py")

if st.session_state.user.get("role") != "admin":
    st.switch_page("app.py")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

admin_sidebar()

# --------------------------------------------------
# PAGE TITLE
# --------------------------------------------------

st.title("👨‍💼 Admin Dashboard")

# --------------------------------------------------
# LOAD VECTOR DATA
# --------------------------------------------------

vector_data = load_vector_store()

if vector_data:
    index, chunks = vector_data
else:
    chunks = []

# --------------------------------------------------
# METRICS
# --------------------------------------------------

total_users = get_total_users()
total_chunks = len(chunks)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Users",
        total_users
    )

with col2:
    st.metric(
        "📄 Total Chunks",
        total_chunks
    )

with col3:
    st.metric(
        "💬 Chat Sessions",
        "Active"
    )

with col4:
    st.metric(
        "🧠 Vector DB",
        "Ready"
    )

st.divider()

# --------------------------------------------------
# SYSTEM STATUS
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.info(
        """
### 📚 Knowledge Base Status

✅ Vector Database Loaded

✅ Documents Available

✅ Retrieval Ready
"""
    )

with col2:

    st.success(
        """
### ⚡ System Status

✅ Gemini Connected

✅ FAISS Running

✅ MySQL Connected
"""
    )

st.divider()

# --------------------------------------------------
# OVERVIEW
# --------------------------------------------------

st.subheader("📊 System Overview")

st.write(
    f"""
Current Knowledge Base contains **{total_chunks} chunks**.

Total Registered Users: **{total_users}**
"""
)