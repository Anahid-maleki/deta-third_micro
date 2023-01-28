from flask import Flask, request, jsonify,redirect,url_for,render_template
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
    c=db.get("three")
    return f"<html><body><h1>{a}   {b}   {c}</h1></body></html>"


@app.route('/signup' , methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email=request.form["email"]
        pas=request.form["psw"]
        db.put({"email":"email","password":"pas","key":"three"})
        return redirect(url_for("success",usr=email))
    else:
      return render_template('signup.html')
    
@app.route("success/<usr>")
def success(usr):
    return f"<html><body><h1>welccome {usr}</h1></body></html>"    
