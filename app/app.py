from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Hello Flask+uWSGI+Nginx+++++++</h2>'

if __name__ == "__main__":
    app.run(host='0.0.0.0')