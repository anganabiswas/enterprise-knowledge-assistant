import streamlit as st

from components.sidebar import admin_sidebar

from database.user_management import (
    get_all_users,
    delete_user
)

from authentication.register_user import (
    create_user
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Manage Users",
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
# PAGE TITLE
# --------------------------------------------------

st.title("👥 User Management")

# --------------------------------------------------
# CREATE USER
# --------------------------------------------------

with st.expander(
    "➕ Create New User",
    expanded=True
):

    username = st.text_input(
        "Username"
    )

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    role = st.selectbox(
        "Role",
        [
            "employee",
            "admin"
        ]
    )

    if st.button(
        "Create User"
    ):

        try:

            create_user(
                username,
                email,
                password,
                role
            )

            st.success(
                "User created successfully."
            )

            st.rerun()

        except Exception as e:

            st.error(str(e))

# --------------------------------------------------
# USERS TABLE
# --------------------------------------------------

st.subheader(
    "Registered Users"
)

users = get_all_users()

header = st.columns(
    [1, 2, 3, 2, 1]
)

header[0].write("ID")
header[1].write("Username")
header[2].write("Email")
header[3].write("Role")
header[4].write("Delete")

st.divider()

for user in users:

    cols = st.columns(
        [1, 2, 3, 2, 1]
    )

    cols[0].write(
        user["id"]
    )

    cols[1].write(
        user["username"]
    )

    cols[2].write(
        user["email"]
    )

    cols[3].write(
        user["role"]
    )

    if (
        user["id"] !=
        st.session_state.user["id"]
    ):

        if cols[4].button(
            "🗑️",
            key=f"user_{user['id']}"
        ):

            delete_user(
                user["id"]
            )

            st.success(
                "User deleted."
            )

            st.rerun()

    st.divider()