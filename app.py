from flask import Flask, render_template,jsonify
from flask_cors import CORS
from pymongo import MongoClient
app = Flask(__name__)
CORS(app, supports_credentials=True)
client = MongoClient('localhost', 27017)
# client["api"]["locations"].insert_one({ 'id': 1, 'lat': 36.4117, 'lon': 35.0818 })
# client["api"]["locations"].insert_one({ 'id': 2, 'lat': 37.2799, 'lon': 37.1297 })
# client["api"]["locations"].insert_one({ 'id': 3, 'lat': 38.2799, 'lon': 37.1297 })
# db = client.flask_db
# todos = db.todos
# client['api']['locations'].delete_many({})
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/getlocations")
def getlocations():
    
    data=list(client['api']['locations'].find({},{'_id':0}))
    print(data)
    return  jsonify(data)

@app.route("/ee")
def ee():
    return "ee"

if __name__ == "__main__":
    app.run()