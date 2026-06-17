from database.db import get_connection


def clear_user_chat_history(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM chat_history
        WHERE user_id = %s
        """,
        (user_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()