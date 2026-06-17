from database.db import get_connection

def login_user(username, password):

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT * FROM users
    WHERE username=%s
    AND password=%s
    """

    cursor.execute(
        query,
        (username, password)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user