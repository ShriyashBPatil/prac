# Program 12b: Employee Management System (Full CRUD) - Flask + MySQL

from flask import Flask, request, redirect, url_for, render_template_string
import mysql.connector

app = Flask(__name__)

# Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',  # Change to your MySQL password
    'database': 'employee_mgmt'
}


def get_db():
    """Get database connection."""
    return mysql.connector.connect(**DB_CONFIG)


def init_db():
    """Initialize database and table."""
    conn = mysql.connector.connect(host='localhost', user='root', password='root')
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS employee_mgmt")
    cursor.execute("USE employee_mgmt")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            department VARCHAR(100),
            salary DECIMAL(10, 2)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()


TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Employee Management System</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #2196F3; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
        form { margin: 20px 0; }
        input, button { padding: 8px; margin: 5px; }
        button { background-color: #2196F3; color: white; border: none; cursor: pointer; }
        button.delete { background-color: #f44336; }
        button.edit { background-color: #FF9800; }
    </style>
</head>
<body>
    <h1>Employee Management System</h1>

    <h2>{{ 'Edit Employee' if edit_employee else 'Add New Employee' }}</h2>
    <form method="POST" action="{{ url_for('update', id=edit_employee.id) if edit_employee else url_for('add') }}">
        <input type="text" name="name" placeholder="Name" value="{{ edit_employee.name if edit_employee else '' }}" required>
        <input type="text" name="department" placeholder="Department" value="{{ edit_employee.department if edit_employee else '' }}" required>
        <input type="number" name="salary" placeholder="Salary" step="0.01" value="{{ edit_employee.salary if edit_employee else '' }}" required>
        <button type="submit">{{ 'Update' if edit_employee else 'Add Employee' }}</button>
    </form>

    <h2>All Employees</h2>
    <table>
        <tr><th>ID</th><th>Name</th><th>Department</th><th>Salary</th><th>Actions</th></tr>
        {% for e in employees %}
        <tr>
            <td>{{ e[0] }}</td><td>{{ e[1] }}</td><td>{{ e[2] }}</td><td>₹{{ e[3] }}</td>
            <td>
                <a href="{{ url_for('edit', id=e[0]) }}"><button class="edit">Edit</button></a>
                <a href="{{ url_for('delete', id=e[0]) }}"><button class="delete">Delete</button></a>
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
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template_string(TEMPLATE, employees=employees, edit_employee=None)


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    department = request.form['department']
    salary = request.form['salary']

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)",
                   (name, department, salary))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))


@app.route('/edit/<int:id>')
def edit(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE id = %s", (id,))
    employee = cursor.fetchone()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    conn.close()

    class EmployeeObj:
        def __init__(self, row):
            self.id, self.name, self.department, self.salary = row

    return render_template_string(TEMPLATE, employees=employees, edit_employee=EmployeeObj(employee))


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    department = request.form['department']
    salary = request.form['salary']

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE employees SET name=%s, department=%s, salary=%s WHERE id=%s",
                   (name, department, salary, id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5001)
