from flask import Flask, request, jsonify
from deta import Deta


deta = Deta('a0ell3iu_GHdFxTWpTdXYphdr9MF2Bro9fxE1W5kJ') # configure your Deta project
db = deta.Base('simpleDB')  # access your DB
app = Flask(__name__)


app=Flask(__name__)    
@app.route('/', methods=['GET'])
def home():
    return f"<html><body><h1>Database</h1></body></html>"
