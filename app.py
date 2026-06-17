import streamlit as st

from authentication.auth_manager import login_user

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    layout="wide"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "user" not in st.session_state:
    st.session_state.user = None

# --------------------------------------------------
# LOGIN PAGE
# --------------------------------------------------

if st.session_state.user is None:

    st.title("📚 Enterprise Knowledge Assistant")

    st.markdown("---")

    st.subheader("🔐 Login")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        user = login_user(
            username,
            password
        )

        if user:

            st.session_state.user = user

            if user["role"] == "admin":

                st.switch_page(
                    "pages/admin_dashboard.py"
                )

            else:

                st.switch_page(
                    "pages/employee_chat.py"
                )

        else:

            st.error(
                "Invalid Username or Password"
            )

    st.stop()

# --------------------------------------------------
# ALREADY LOGGED IN
# --------------------------------------------------

if st.session_state.user["role"] == "admin":

    st.switch_page(
        "pages/admin_dashboard.py"
    )

else:

    st.switch_page(
        "pages/employee_chat.py"
    )