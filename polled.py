import counter
from flask import Flask
from flask import session
app = Flask(__name__)

@app.route("/")
def hello():
    if  counter.getCount("counter") == 5:
        counter.reset("counter") 
        return "y"
    else:
        counter.increment("counter") 
        return "n"

