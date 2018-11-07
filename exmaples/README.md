Examples
========

Hello
-----

1. Initialize your logger database
```
$ FLASK_APP=hello.py flask logger init_db --app=hello 
```
1. Run the hello Flask app
```
$ FLASK_APP=hello.py flask run
```
3. By visiting http://localhost:5000/, will log the requests/responses in request_log.db.