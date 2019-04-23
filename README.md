Flask Request Logger
====================
[![Build Status](https://img.shields.io/drone/build/BbsonLin/flask-request-logger.svg?style=flat-square)](https://cloud.drone.io/BbsonLin/flask-request-logger)
[![Build Status](https://img.shields.io/travis/BbsonLin/flask-request-logger.svg?style=flat-square)](https://travis-ci.org/BbsonLin/flask-request-logger)
[![Documentation Status](https://img.shields.io/readthedocs/flask-request-logger/latest.svg?style=flat-square)](https://flask-request-logger.readthedocs.io/en/latest/)
[![image](https://img.shields.io/pypi/v/flask-request-logger.svg?style=flat-square)](https://pypi.org/project/flask-request-logger/)
[![image](https://img.shields.io/pypi/status/flask-request-logger.svg?style=flat-square)](https://pypi.org/project/flask-request-logger/)
[![image](https://img.shields.io/pypi/l/flask-request-logger.svg?style=flat-square)](https://pypi.org/project/flask-request-logger/)
[![image](https://img.shields.io/pypi/pyversions/flask-request-logger.svg?style=flat-square)](https://pypi.org/project/flask-request-logger/)


**This module is in Development Status :: 3 - Alpha**

Flask-Request-Logger is an extension for [Flask](http://flask.pocoo.org/) that logging requests and responses for your Flask app.

Compatibility
-------------

For now Python 3.5+.

Installation
------------

With pip:
```
$ pip install flask-reqeust-logger
```

Testing
-------

Run unittest in current development environment
```
$ pytest -sv --tap-combined
```
* `--tap-combined` option will log the test result in testresults.tap.  
* More testing options please check [pytest](https://github.com/pytest-dev/pytest/), [pytest-tap](https://github.com/python-tap/pytest-tap) or more [pytest plugins](http://plugincompat.herokuapp.com/)
