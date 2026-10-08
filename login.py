import sqlite3
from database import create_connection


def login():

    print("\n================================")
    print("       COLLEGE ERP LOGIN")
    print("================================")

    username = input("Username: ")
    password = input("Password: ")

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_id, user_name, role
        FROM users
        WHERE user_name = ? AND password = ?
    """, (username, password))

    user = cursor.fetchone()

    conn.close()

    if user:
        print("\nLogin Successful!")
        print("Welcome", username)

        return user

    else:
        print("\nInvalid username or password!")
        return None