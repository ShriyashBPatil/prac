from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # You can change the marks here to test
    return render_template('pass_fail.html', marks=65)

if __name__ == '__main__':
    app.run(debug=True)
