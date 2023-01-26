from flask import Flask, request, jsonify
from deta import Deta

app=Flask(__name__)


# Initialize with a Project Key
deta = Deta("a0ell3iu_AFmGiAybnBeSffX3WgzPBgd1EtKfkz6s")

# This how to connect to or create a database.
db = deta.Base("first_db")

# You can create as many as you want without additional charges.
books = deta.Base("books")


@app.route('/', methods=['GET'])
def home():
    return f"<html><body><h1>Database</h1></body></html>"
