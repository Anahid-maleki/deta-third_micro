from flask import Flask, request, jsonify
from deta import Deta

app=Flask(__name__)



deta = Deta('myProjectKey') # configure your Deta project
db = deta.Base('simpleDB')  # access your DB
app = Flask(__name__)

{
    "name": str,
    "age": int,
    "hometown": str
}

@app.route('/users', methods=["POST"])
def create_user():
    name = request.json.get("name")
    age = request.json.get("age")
    hometown = request.json.get("hometown")
    
    user = db.put({
        "name": name,
        "age": age,
        "hometown": hometown
    })

    return jsonify(user, 201)

@app.route('/', methods=['GET'])
def home():
    return f"<html><body><h1>Database</h1></body></html>"
