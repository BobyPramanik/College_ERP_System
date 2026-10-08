import sqlite3

def create_connection() -> sqlite3.Connection:
    return sqlite3.connect("college_erp.db")

def create_tables():    
    con: sqlite3.Connection = create_connection()
    cursor: sqlite3.Cursor = con.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students(
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE NOT NULL,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            department TEXT,
            semester INTEGER,

            FOREIGN KEY (user_id) 
            REFERENCES users(user_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers(
            teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE NOT NULL,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            department TEXT,
            subjects TEXT,
                
            FOREIGN KEY (user_id) 
            REFERENCES users(user_id)
        )
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO users (user_name, password, role)
        VALUES(?, ?, ?)
        ''', ("admin", "admin123", "admin"))

    con.commit()
    con.close()


create_table = create_tables
