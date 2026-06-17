from database.db import get_connection

def get_total_users():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total