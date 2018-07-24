import counter
from flask import Flask
from multiprocessing import Process
import poller

def poll():
    polling_process = Process(target=poller.run)
    polling_process.start()

poll()
app = Flask(__name__)
@app.route("/")
def hello():
    return str(counter.getCount("ycounter"))

