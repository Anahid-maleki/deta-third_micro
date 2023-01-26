from flask import Flask, request, jsonify
from deta import Deta

app=Flask(__name__)

deta = Deta('a0ell3iu_erjdV8yDHpSTugkvFa9ma6wp11WMF8zt') # configure your Deta project
db1 = deta.Base("bd1")

db1.insert({
    "name": "Anahid",
    "title": "developer"
})

fetch_res = db1.fetch({"name": "Anahid"})

# for item in fetch_res.items:
#     db1.delete(item["key"])

@app.route('/', methods=['GET'])
def home():
    return f"<html><body><h1>Database</h1></body></html>"
