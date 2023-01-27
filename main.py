from flask import Flask, request, jsonify
from deta import Deta

deta = Deta("a0ell3iu_GHdFxTWpTdXYphdr9MF2Bro9fxE1W5kJ")  
db = deta.Base("simple_db")


app=Flask(__name__)    
@app.route('/', methods=['GET'])
def home():
    db.put({"name": "Anahid","key":"one"})
    a=db.get("name") 
    return f"<html><body><h1>{a}</h1></body></html>"
