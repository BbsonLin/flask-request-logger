from flask import Flask
from flask_request_logger import RequestLogger

app = Flask('hello')
req_logger = RequestLogger(app)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return 'hello'
