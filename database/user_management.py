from database.db import get_connection


def get_all_users():

    conn = get_connection()

    cursor = conn.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT
            id,
            username,
            email,
            role,
            created_at
        FROM users
        ORDER BY id DESC
        """
    )

    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users


def delete_user(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM users
        WHERE id = %s
        """,
        (user_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()