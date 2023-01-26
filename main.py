from flask import Flask, request, jsonify
from deta import Deta

app=Flask(__name__)
# deta = Deta('myProjectKey') # configure your Deta project
# db = deta.Base('simpleDB')  # access your DB

@app.route('/', methods=['GET'])
def home():
    return f"<html><body><h1>Hello to you</h1></body></html>"
