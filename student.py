from database import create_connection


def student_dashboard(user_id):

    while True:

        print("\n================================")
        print("        STUDENT DASHBOARD")
        print("================================")

        print("1. View My Profile")
        print("2. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            view_profile(user_id)

        elif choice == "2":
            print("Student logged out.")
            break

        else:
            print("Invalid choice!")


def view_profile(user_id):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, email, phone,
               department, semester
        FROM students
        WHERE user_id = ?
    """, (user_id,))

    student = cursor.fetchone()

    if student:

        print("\n========== MY PROFILE ==========")

        print("Name       :", student[0])
        print("Email      :", student[1])
        print("Phone      :", student[2])
        print("Department :", student[3])
        print("Semester   :", student[4])

        conn.close()