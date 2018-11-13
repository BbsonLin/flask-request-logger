Flask Request Logger
====================

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
