# Program 10a: Simple form using the GET method

from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>GET Form</title></head>
<body>
    <h1>Simple GET Form</h1>
    <form method="GET" action="/result">
        <label>Enter your name: </label>
        <input type="text" name="name" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

RESULT_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Result</title></head>
<body>
    <h1>Hello, {{ name }}!</h1>
    <p>Data received via GET method.</p>
    <a href="/">Go Back</a>
</body>
</html>
"""


@app.route('/')
def form():
    return render_template_string(TEMPLATE)


@app.route('/result')
def result():
    name = request.args.get('name', 'Guest')
    return render_template_string(RESULT_TEMPLATE, name=name)


if __name__ == '__main__':
    app.run(debug=True)
