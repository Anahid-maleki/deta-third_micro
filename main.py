from flask import Flask, request, jsonify




# 1) pip install deta
from deta import Deta

# 2) initialize with a project key
deta = Deta("a0ell3iu_GHdFxTWpTdXYphdr9MF2Bro9fxE1W5kJ")

# 3) create and use as many DBs as you want!
users = deta.Base("users")

users.insert({
    "name": "Geordi",
    "title": "Chief Engineer"
})

fetch_res = users.fetch({"name": "Geordi"})

for item in fetch_res.items:
    users.delete(item["key"])

app=Flask(__name__)    
@app.route('/', methods=['GET'])
def home():
    return f"<html><body><h1>Database</h1></body></html>"
