# Program 11: MySQL Integration with Python
# a) Connect to MySQL
# b) Create Database
# c) Create Table
# d) Insert Records
# e) Fetch Records
# f) Update Records
# g) Delete Records

import mysql.connector

# ============================================================
# a) Connect to MySQL Server
# ============================================================
def connect_to_mysql():
    """Connect to MySQL server."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"  # Change this to your MySQL password
    )
    print("✓ Connected to MySQL Server successfully!")
    return conn


# ============================================================
# b) Create Database
# ============================================================
def create_database(conn):
    """Create a database named 'student_db'."""
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
    print("✓ Database 'student_db' created successfully!")
    cursor.close()


# ============================================================
# c) Create Table
# ============================================================
def create_table(conn):
    """Create a 'students' table."""
    cursor = conn.cursor()
    cursor.execute("USE student_db")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            branch VARCHAR(100),
            marks INT
        )
    """)
    print("✓ Table 'students' created successfully!")
    cursor.close()


# ============================================================
# d) Insert Records
# ============================================================
def insert_records(conn):
    """Insert student records into the table."""
    cursor = conn.cursor()
    cursor.execute("USE student_db")

    students = [
        ("Shriyash", "Computer Science", 85),
        ("Rahul", "IT", 90),
        ("Priya", "Electronics", 78),
        ("Amit", "Mechanical", 65),
        ("Neha", "Civil", 92),
    ]

    query = "INSERT INTO students (name, branch, marks) VALUES (%s, %s, %s)"
    cursor.executemany(query, students)
    conn.commit()
    print(f"✓ {cursor.rowcount} records inserted successfully!")
    cursor.close()


# ============================================================
# e) Fetch Records
# ============================================================
def fetch_records(conn):
    """Fetch and display all student records."""
    cursor = conn.cursor()
    cursor.execute("USE student_db")
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\n--- Student Records ---")
    print(f"{'ID':<5}{'Name':<15}{'Branch':<20}{'Marks':<10}")
    print("-" * 50)
    for row in records:
        print(f"{row[0]:<5}{row[1]:<15}{row[2]:<20}{row[3]:<10}")
    cursor.close()


# ============================================================
# f) Update Records
# ============================================================
def update_record(conn, student_id, new_marks):
    """Update marks for a student."""
    cursor = conn.cursor()
    cursor.execute("USE student_db")
    query = "UPDATE students SET marks = %s WHERE id = %s"
    cursor.execute(query, (new_marks, student_id))
    conn.commit()
    print(f"✓ Student ID {student_id} updated to marks {new_marks}!")
    cursor.close()


# ============================================================
# g) Delete Records
# ============================================================
def delete_record(conn, student_id):
    """Delete a student record."""
    cursor = conn.cursor()
    cursor.execute("USE student_db")
    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()
    print(f"✓ Student ID {student_id} deleted successfully!")
    cursor.close()


# ============================================================
# Main Execution
# ============================================================
if __name__ == '__main__':
    # a) Connect
    conn = connect_to_mysql()

    # b) Create Database
    create_database(conn)

    # c) Create Table
    create_table(conn)

    # d) Insert Records
    insert_records(conn)

    # e) Fetch Records
    fetch_records(conn)

    # f) Update Record (update student ID 1 marks to 95)
    update_record(conn, 1, 95)
    fetch_records(conn)

    # g) Delete Record (delete student ID 4)
    delete_record(conn, 4)
    fetch_records(conn)

    # Close connection
    conn.close()
    print("\n✓ Connection closed.")
