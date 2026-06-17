import streamlit as st

# --------------------------------------------------
# ADMIN SIDEBAR
# --------------------------------------------------

def admin_sidebar():

    st.sidebar.title("🏢 Knowledge Assistant")
    st.sidebar.caption("Admin Portal")

    if st.session_state.get("user"):
        st.sidebar.success(f"🛡️ {st.session_state.user['username']}")

    st.sidebar.write("Administrator")
    st.sidebar.divider()

    if st.sidebar.button("🏠 Dashboard"):
        st.switch_page("pages/admin_dashboard.py")

    if st.sidebar.button("📤 Upload Documents"):
        st.switch_page("pages/upload_documents.py")

    if st.sidebar.button("👥 Manage Users"):
        st.switch_page("pages/manage_users.py")

    if st.sidebar.button("📊 Analytics"):
        st.switch_page("pages/analytics.py")

    if st.sidebar.button("🤖 Chat with AI"):
        st.switch_page("pages/employee_chat.py")

    if st.sidebar.button("🕒 Chat History"):
        st.switch_page("pages/chat_history.py")

    if st.sidebar.button("🚪 Logout"):
        st.session_state.user = None
        st.switch_page("app.py")


# --------------------------------------------------
# EMPLOYEE SIDEBAR
# --------------------------------------------------

def employee_sidebar():

    st.sidebar.title("🏢 Knowledge Assistant")
    st.sidebar.caption("Employee Portal")

    if st.session_state.get("user"):
        st.sidebar.success(f"👤 {st.session_state.user['username']}")

    st.sidebar.write("Knowledge User")
    st.sidebar.divider()

    if st.sidebar.button("🤖 Chat with AI"):
        st.switch_page("pages/employee_chat.py")

    if st.sidebar.button("🕒 Chat History"):
        st.switch_page("pages/chat_history.py")

    if st.sidebar.button("🚪 Logout"):
        st.session_state.user = None
        st.switch_page("app.py")