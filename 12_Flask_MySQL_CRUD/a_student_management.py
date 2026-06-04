# Program 12a: Student Management System (Full CRUD) - Flask + MySQL

from flask import Flask, request, redirect, url_for, render_template_string
import mysql.connector

app = Flask(__name__)

# Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',  # Change to your MySQL password
    'database': 'student_mgmt'
}


def get_db():
    """Get database connection."""
    return mysql.connector.connect(**DB_CONFIG)


def init_db():
    """Initialize database and table."""
    conn = mysql.connector.connect(host='localhost', user='root', password='root')
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS student_mgmt")
    cursor.execute("USE student_mgmt")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            branch VARCHAR(100),
            marks INT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()


TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Management System</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #4CAF50; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
        form { margin: 20px 0; }
        input, button { padding: 8px; margin: 5px; }
        button { background-color: #4CAF50; color: white; border: none; cursor: pointer; }
        button.delete { background-color: #f44336; }
        button.edit { background-color: #2196F3; }
    </style>
</head>
<body>
    <h1>Student Management System</h1>

    <h2>{{ 'Edit Student' if edit_student else 'Add New Student' }}</h2>
    <form method="POST" action="{{ url_for('update', id=edit_student.id) if edit_student else url_for('add') }}">
        <input type="text" name="name" placeholder="Name" value="{{ edit_student.name if edit_student else '' }}" required>
        <input type="text" name="branch" placeholder="Branch" value="{{ edit_student.branch if edit_student else '' }}" required>
        <input type="number" name="marks" placeholder="Marks" value="{{ edit_student.marks if edit_student else '' }}" required>
        <button type="submit">{{ 'Update' if edit_student else 'Add Student' }}</button>
    </form>

    <h2>All Students</h2>
    <table>
        <tr><th>ID</th><th>Name</th><th>Branch</th><th>Marks</th><th>Actions</th></tr>
        {% for s in students %}
        <tr>
            <td>{{ s[0] }}</td><td>{{ s[1] }}</td><td>{{ s[2] }}</td><td>{{ s[3] }}</td>
            <td>
                <a href="{{ url_for('edit', id=s[0]) }}"><button class="edit">Edit</button></a>
                <a href="{{ url_for('delete', id=s[0]) }}"><button class="delete">Delete</button></a>
            </td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""


@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template_string(TEMPLATE, students=students, edit_student=None)


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    branch = request.form['branch']
    marks = request.form['marks']

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, branch, marks) VALUES (%s, %s, %s)",
                   (name, branch, marks))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))


@app.route('/edit/<int:id>')
def edit(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
    student = cursor.fetchone()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()

    class StudentObj:
        def __init__(self, row):
            self.id, self.name, self.branch, self.marks = row

    return render_template_string(TEMPLATE, students=students, edit_student=StudentObj(student))


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    branch = request.form['branch']
    marks = request.form['marks']

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=%s, branch=%s, marks=%s WHERE id=%s",
                   (name, branch, marks, id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
