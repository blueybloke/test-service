from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "It's sunny I guess 🤷‍♀️☀🌞"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=False)
