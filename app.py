from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='localhost', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'v3/Hello World! I have been seen {} times.\n'.format(count)

@app.route('/healthcheck')
def hello():
    return 'OK'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
