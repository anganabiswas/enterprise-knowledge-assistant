from database.db import get_connection

def create_user(
    username,
    email,
    password,
    role
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (username,email,password,role)
        VALUES (%s,%s,%s,%s)
        """,
        (
            username,
            email,
            password,
            role
        )
    )

    conn.commit()

    cursor.close()
    conn.close()