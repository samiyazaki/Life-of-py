from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_info = {}
    if request.method == 'POST':
        user_info = {
            'name': request.form.get('name'),
            'color': request.form.get('color'),
            'food': request.form.get('food'),
            'hobby': request.form.get('hobby'),
        }
        greetings = [
            "Hello, {}! It's great to see you.",
            "Hi, {}! Hope you're having a good day.",
            "Hey, {}! What's up?",
            "Good to see you, {}! How have you been?",
            "Hello, {}! Nice to meet you.",
            "How you doin', {}?"
        ]
        random_greeting = random.choice(greetings)
        user_info['greeting'] = random_greeting.format(user_info['name'])

    return render_template('index.html', user_info=user_info)

if __name__ == '__main__':
    app.run(debug=True)
