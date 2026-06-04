# Program 10d: Registration form with validation

from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Registration Form</title></head>
<body>
    <h1>Registration Form</h1>
    {% if errors %}
        <ul style="color: red;">
        {% for err in errors %}
            <li>{{ err }}</li>
        {% endfor %}
        </ul>
    {% endif %}
    {% if success %}
        <p style="color: green;">{{ success }}</p>
    {% endif %}

    <form method="POST">
        <label>Name: </label>
        <input type="text" name="name"><br><br>
        <label>Email: </label>
        <input type="text" name="email"><br><br>
        <label>Password: </label>
        <input type="password" name="password"><br><br>
        <label>Confirm Password: </label>
        <input type="password" name="confirm_password"><br><br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def register():
    errors = []
    success = None

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm_password', '')

        if not name:
            errors.append("Name is required.")
        if not email or '@' not in email:
            errors.append("Valid email is required.")
        if len(password) < 6:
            errors.append("Password must be at least 6 characters.")
        if password != confirm:
            errors.append("Passwords do not match.")

        if not errors:
            success = f"Registration successful! Welcome, {name}."

    return render_template_string(TEMPLATE, errors=errors, success=success)


if __name__ == '__main__':
    app.run(debug=True)
