from flask import Flask, request, jsonify
from deta import Deta

app=Flask(__name__)

deta = Deta('a0ell3iu_erjdV8yDHpSTugkvFa9ma6wp11WMF8zt') # configure your Deta project
users = deta.Base("first_db")

# users.insert({
#     "name": "",
#     "title": "Chief Engineer"
# })

# fetch_res = users.fetch({"name": "Geordi"})

# for item in fetch_res.items:
#     users.delete(item["key"])

@app.route('/', methods=['GET'])
def home():
    return f"<html><body><h1>Database</h1></body></html>"
