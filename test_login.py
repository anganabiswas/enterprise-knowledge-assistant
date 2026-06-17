from authentication.auth_manager import login_user

user = login_user(
    "admin",
    "admin123"
)

print(user)