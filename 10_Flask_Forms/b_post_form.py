# Program 10b: Form using the POST method

from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>POST Form</title></head>
<body>
    <h1>POST Method Form</h1>
    <form method="POST">
        <label>Enter your name: </label>
        <input type="text" name="name" required><br><br>
        <label>Enter your email: </label>
        <input type="email" name="email" required><br><br>
        <button type="submit">Submit</button>
    </form>

    {% if name %}
        <h2>Submitted Data:</h2>
        <p>Name: {{ name }}</p>
        <p>Email: {{ email }}</p>
    {% endif %}
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def form():
    name = email = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
    return render_template_string(TEMPLATE, name=name, email=email)


if __name__ == '__main__':
    app.run(debug=True)
