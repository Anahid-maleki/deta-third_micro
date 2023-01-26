from flask import Flask, request, jsonify
from deta import Deta

deta = Deta("a0ell3iu_GHdFxTWpTdXYphdr9MF2Bro9fxE1W5kJ")  
db = deta.Base("simple_db")

db.put({"test": "test"})

app=Flask(__name__)    
@app.route('/', methods=['GET'])
def home():
    return f"<html><body><h1>making database</h1></body></html>"
