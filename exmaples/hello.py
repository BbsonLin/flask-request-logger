import os

from flask import Flask
from flask_request_logger import RequestLogger

app = Flask('hello')
app.config['REQUEST_LOGGER_DB_URI'] = os.getenv('REQUEST_LOGGER_DB_URI')
req_logger = RequestLogger(app)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)
