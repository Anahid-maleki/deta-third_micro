from flask import Flask, request, jsonify
from deta import Deta



# 2) initialize with a project key
deta = Deta("a0ell3iu_1R3RhxZppEoGsHU2p36Ehhg22nM7xLFP")

# 3) create and use as many DBs as you want!
db = deta.Base("users")

app=Flask(__name__)

# users.insert({
#     "name": "Geordi",
#     "title": "Chief Engineer"
# })

# fetch_res = users.fetch({"name": "Geordi"})

# for item in fetch_res.items:
#     users.delete(item["key"])

@app.route('/', methods=['GET'])
def home():
    return f"<html><body><h1>Database</h1></body></html>"
