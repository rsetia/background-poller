import requests
import counter
url = "http://localhost:8081"

def run():
    while True:
        r = requests.get(url)
        if r.text == "y":
            counter.increment("ycounter")
