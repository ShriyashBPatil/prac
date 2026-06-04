from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    return f"<h1>Hello, {username}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
