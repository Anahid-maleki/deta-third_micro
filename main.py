from flask import Flask, request, jsonify
from deta import Deta

deta = Deta("a0ell3iu_GHdFxTWpTdXYphdr9MF2Bro9fxE1W5kJ")  
db = deta.Base("simple_db")


app=Flask(__name__)    
@app.route('/', methods=['GET'])
def home():
    db.put({"test": "test"}) 
    return f"<html><body><h1>making database</h1></body></html>"
