import sqlite3
from database import create_connection


def admin_dashboard():

    while True:

        print("\n================================")
        print("          ADMIN DASHBOARD")
        print("================================")

        print("1. Add Teacher")
        print("2. Add Student")
        print("3. View Teachers")
        print("4. View Students")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            add_teacher()

        elif choice == "2":
            add_student()

        elif choice == "3":
            view_teachers()

        elif choice == "4":
            view_students()

        elif choice == "5":
            print("Admin logged out.")
            break

        else:
            print("Invalid choice!")


def add_teacher():

    print("\n----- ADD TEACHER -----")

    username = input("Username: ")
    password = input("Password: ")

    name  = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    department = input("Department: ")
    subjects = input("Subject: ")

    conn = create_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            INSERT INTO users
            (user_name, password, role)
            VALUES (?, ?, ?)
        """, (username, password, "teacher"))

        user_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO teachers
            (user_id, name, email, phone, department, subjects)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            name,
            email,
            phone,
            department,
            subjects
        ))

        conn.commit()

        print("\nTeacher added successfully!")

    except sqlite3.IntegrityError:
        print("\nUsername or email already exists!")

    conn.close()


def add_student():

    print("\n----- ADD STUDENT -----")

    username = input("Username: ")
    password = input("Password: ")

    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    department = input("Department: ")
    semester:int = int(input("Semester: "))

    conn = create_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            INSERT INTO users
            (user_name, password, role)
            VALUES (?, ?, ?)
        """, (username, password, "student"))

        user_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO students
            (user_id, name, email, phone, department, semester)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            name,
            email,
            phone,
            department,
            semester
        ))

        conn.commit()

        print("\nStudent added successfully!")

    except sqlite3.IntegrityError:
        print("\nUsername or email already exists!")

    conn.close()


def view_teachers():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT teacher_id, name, email,
               phone, department, subjects
        FROM teachers
    """)

    teachers = cursor.fetchall()

    print("\n========== TEACHERS ==========")

    for teacher in teachers:

        print(
            f"""
Teacher ID : {teacher[0]}
Name       : {teacher[1]}
Email      : {teacher[2]}
Phone      : {teacher[3]}
Department : {teacher[4]}
Subject    : {teacher[5]}
-------------------------------
"""
        )

    conn.close()


def view_students():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id, name, email,
               phone, department, semester
        FROM students
    """)

    students = cursor.fetchall()

    print("\n========== STUDENTS ==========")

    for student in students:

        print(
            f"""
Student ID : {student[0]}
Name       : {student[1]}
Email      : {student[2]}
Phone      : {student[3]}
Department : {student[4]}
Semester   : {student[5]}
-------------------------------
"""
        )

    conn.close()