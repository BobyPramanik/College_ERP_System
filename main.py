from database import create_tables
from login import login
from admin import admin_dashboard
from teacher import teacher_dashboard
from student import student_dashboard


def main():

    # Create database and tables
    create_tables()

    while True:

        print("\n================================")
        print("       COLLEGE ERP SYSTEM")
        print("================================")

        print("1. Login")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            user = login()

            if user:

                user_id = user[0]
                role = user[2]

                if role == "admin":
                    admin_dashboard()

                elif role == "teacher":
                    teacher_dashboard(user_id)

                elif role == "student":
                    student_dashboard(user_id)

        elif choice == "2":

            print("\nThank you for using College ERP!")
            break

        else:

            print("Invalid choice!")


if __name__ == "__main__":
    main()