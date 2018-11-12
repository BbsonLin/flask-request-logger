Examples
========

Hello
-----

1. Initialize your logger database
```
$ FLASK_APP=hello.py flask logger init_db --app=hello 
```
2. Run the hello Flask app
```
$ FLASK_APP=hello.py flask run
```
3. By visiting http://localhost:5000/, will log the requests/responses in request_log.db.


Flaskr
------
This project is provided by [Flask's Tutorial](http://flask.pocoo.org/docs/1.0/tutorial/).

1. Initialize your logger database
```
$ FLASK_APP=flaskr flask logger init_db --app=flaskr 
```
2. Run Flaskr app
```
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask init-db
$ flask run
```
