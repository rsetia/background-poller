import redis

def r():
    return redis.StrictRedis(host='localhost', port=6379, db=0)

def get_key(key):
    return key

def increment(key):
    return r().incr(get_key(key))

def getCount(key):
    c = r().get(get_key(key)) 
    return int(c) if c else 0

def reset(key):
    return r().delete(get_key(key))

