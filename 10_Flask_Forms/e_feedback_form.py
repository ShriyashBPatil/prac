# Program 10e: Feedback form using textarea and radio buttons

from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Feedback Form</title></head>
<body>
    <h1>Feedback Form</h1>

    {% if feedback %}
        <h2>Submitted Feedback:</h2>
        <p><strong>Name:</strong> {{ feedback.name }}</p>
        <p><strong>Rating:</strong> {{ feedback.rating }}</p>
        <p><strong>Comments:</strong> {{ feedback.comments }}</p>
        <hr>
    {% endif %}

    <form method="POST">
        <label>Name: </label>
        <input type="text" name="name" required><br><br>

        <label>Rating: </label><br>
        <input type="radio" name="rating" value="Excellent" required> Excellent<br>
        <input type="radio" name="rating" value="Good"> Good<br>
        <input type="radio" name="rating" value="Average"> Average<br>
        <input type="radio" name="rating" value="Poor"> Poor<br><br>

        <label>Comments: </label><br>
        <textarea name="comments" rows="4" cols="40" required></textarea><br><br>

        <button type="submit">Submit Feedback</button>
    </form>
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def feedback():
    feedback_data = None
    if request.method == 'POST':
        feedback_data = {
            'name': request.form.get('name'),
            'rating': request.form.get('rating'),
            'comments': request.form.get('comments')
        }
    return render_template_string(TEMPLATE, feedback=feedback_data)


if __name__ == '__main__':
    app.run(debug=True)
