import sqlite3
from database import create_connection


def teacher_dashboard(user_id):

    while True:

        print("\n================================")
        print("        TEACHER DASHBOARD")
        print("================================")

        print("1. View My Profile")
        print("2. View Students")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            view_profile(user_id)

        elif choice == "2":
            view_students()

        elif choice == "3":
            print("Teacher logged out.")
            break

        else:
            print("Invalid choice!")


def view_profile(user_id):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, email, phone,
               department, subjects
        FROM teachers
        WHERE user_id = ?
    """, (user_id,))

    teacher = cursor.fetchone()

    conn.close()

    if teacher:

        print("\n========== MY PROFILE ==========")

        print("Name       :", teacher[0])
        print("Email      :", teacher[1])
        print("Phone      :", teacher[2])
        print("Department :", teacher[3])
        print("Subject    :", teacher[4])


def view_students():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id, name,
               department, semester
        FROM students
    """)

    students = cursor.fetchall()

    print("\n========== STUDENTS ==========")

    for student in students:

        print(
            f"""
ID         : {student[0]}
Name       : {student[1]}
Department : {student[2]}
Semester   : {student[3]}
"""
        )

    conn.close()