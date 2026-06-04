# Program 10c: Login form with validation

from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Login Form</title></head>
<body>
    <h1>Login Form</h1>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
    {% if success %}
        <p style="color: green;">{{ success }}</p>
    {% endif %}

    <form method="POST">
        <label>Username: </label>
        <input type="text" name="username" required><br><br>
        <label>Password: </label>
        <input type="password" name="password" required><br><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def login():
    error = success = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == 'admin123':
            success = f"Welcome, {username}! Login successful."
        else:
            error = "Invalid username or password!"

    return render_template_string(TEMPLATE, error=error, success=success)


if __name__ == '__main__':
    app.run(debug=True)
