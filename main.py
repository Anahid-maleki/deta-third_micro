from flask import Flask, request, jsonify
from deta import Deta

app=Flask(__name__)

# 2) initialize with a project key
deta = Deta("project key")

# 3) create and use as many DBs as you want!
users = deta.Base("users")

@app.route('/', methods=['GET'])
def home():
    return f"<html><body><h1>Database</h1></body></html>"
