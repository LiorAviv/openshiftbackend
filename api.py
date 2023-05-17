from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/getlocations")
def getlocations():
    return [
    { 'id': 1, 'lat': 36.4117, 'lon': 35.0818 },
    { 'id': 2, 'lat': 37.2799, 'lon': 37.1297 },
    { 'id': 3, 'lat': 38.2799, 'lon': 37.1297 },
    ]

@app.route("/ee")
def ee():
    return "ee"

if __name__ == "__main__":
    app.run()