from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    subject_list = ["Math", "Science", "History", "English"]
    return render_template('subjects.html', subjects=subject_list)

if __name__ == '__main__':
    app.run(debug=True)
