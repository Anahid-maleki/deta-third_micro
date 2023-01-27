from flask import Flask, request, jsonify
from deta import Deta

deta = Deta("a0ell3iu_GHdFxTWpTdXYphdr9MF2Bro9fxE1W5kJ")  
db = deta.Base("simple_db")


app=Flask(__name__)    
@app.route('/', methods=['GET'])
def home():
    db.put({"name": "Anahid","key":"one"})
    db.put({"name": "alex", "age": 77, "key": "two"})
    a=db.get("one") 
    b=db.get("two")
    return f"<html><body><h1>{a}   {b}</h1></body></html>"
