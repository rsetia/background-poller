# Request a poller

Project contains two servers. 

One server will increment a counter in Redis each time a request is made to it. When that counter 
    reaches 5 it resets the counter. If the counter is currently 5 it returns "y" otherwise "n"
    in the response body. 

Another server will launch a poller in the background whose job is to poll the server above.
    When this poller sees a "y" response it increments another counter in redis. 

This simulates a poller performing an action after polling an endpoint. 

The second server will also have an endpoint where the second counter can be queried (ie. the user can get
    the amount of times "y" was seen by the poller.


# running

The polled server;
`FLASK_APP=polled.py flask run -p 8081`

The server exposing the "y" counter:
`FLASK_APP=server.py flask run` 

# Make a request
curl localhost:5000


