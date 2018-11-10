=============
Basic Example
=============

You can check out this example's source from `Here`_.

You can also check out how to run this example from `README`_. 

.. code-block:: python

    from flask import Flask
    from flask_request_logger import RequestLogger

    app = Flask('hello')
    req_logger = RequestLogger(app)


    @app.route('/', methods=['GET', 'POST'])
    def hello():
        return 'hello'

.. _Here: https://github.com/BbsonLin/flask-request-logger/blob/master/exmaples/hello.py
.. _README: https://github.com/BbsonLin/flask-request-logger/blob/master/exmaples/README.md#hello