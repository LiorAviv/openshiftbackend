from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/e")
def e():
    return "e"

@app.route("/ee")
def ee():
    return "ee"

if __name__ == "__main__":
    app.run()