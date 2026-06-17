import mysql.connector

def get_connection():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Angana@sql1",
        database="enterprise_knowledge_assistant"
    )