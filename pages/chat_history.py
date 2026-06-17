import streamlit as st

from components.sidebar import (
    admin_sidebar,
    employee_sidebar
)

from database.chat_history import (
    get_user_chats
)

from database.chat_management import (
    clear_user_chat_history
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Chat History",
    layout="wide"
)

# --------------------------------------------------
# LOGIN CHECK
# --------------------------------------------------

if "user" not in st.session_state:

    st.switch_page("app.py")

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

st.title("🕒 Chat History")

# --------------------------------------------------
# CLEAR HISTORY
# --------------------------------------------------

if st.button(
    "🗑 Clear Chat History"
):

    clear_user_chat_history(
        st.session_state.user["id"]
    )

    st.success(
        "Chat History Deleted Successfully"
    )

    st.rerun()

st.divider()

# --------------------------------------------------
# LOAD CHAT HISTORY
# --------------------------------------------------

user_chats = get_user_chats(
    st.session_state.user["id"]
)

if user_chats:

    for chat in user_chats:

        with st.container():

            st.markdown(
                f"### 🧑 Question"
            )

            st.write(
                chat["question"]
            )

            st.markdown(
                f"### 🤖 Answer"
            )

            st.write(
                chat["answer"]
            )

            st.caption(
                f"🕒 {chat['created_at']}"
            )

            st.divider()

else:

    st.info(
        "No chat history found."
    )