from database.db import get_connection

def save_chat(
    user_id,
    question,
    answer
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chat_history
        (user_id,question,answer)
        VALUES (%s,%s,%s)
        """,
        (
            user_id,
            question,
            answer
        )
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_user_chats(
    user_id
):

    conn = get_connection()

    cursor = conn.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT *
        FROM chat_history
        WHERE user_id=%s
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data