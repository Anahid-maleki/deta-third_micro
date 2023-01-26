from flask import Flask, request, jsonify
from deta import Deta


from deta import Deta
deta = Deta("project key")  
db = deta.Base("simple_db")

# store objects
# a key will be automatically generated
db.put({"name": "alex", "age": 77})  
# we will use "one" as a key
db.put({"name": "alex", "age": 77}, "one")  
# the key could also be included in the object itself  
db.put({"name": "alex", "age": 77, "key": "one"})

# simple types
db.put("hello, worlds")
db.put(7)
# "success" is the value and "smart_work" is the key.
db.put("success", "smart_work")  
db.put(["a", "b", "c"], "my_abc")

# expiring items
# expire item in 300 seconds
db.put({"name": "alex", "age": 23}, "alex23", expire_in=300)
# expire item at date
expire_at = datetime.datetime.fromisoformat("2023-01-01T00:00:00")
db.put({"name": "max", "age": 28}, "max28", expire_at=expire_at)
app=Flask(__name__)    
@app.route('/', methods=['GET'])
def home():
    return f"<html><body><h1>Database</h1></body></html>"
