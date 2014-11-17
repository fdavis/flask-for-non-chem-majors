demo flask app from [Beginning Web Development with Python by Andrei Dan](http://www.amazon.com/Beginning-Web-Development-Python-production-ebook/dp/B00N8YB0CW)

If you have docker and the code setup at ./flaskapp you can

1. docker run -i -t -v `pwd`/flaskapp:/opt/flaskapp -p 1337:1337 fdavis/utopic-flask-tut /opt/flaskapp/run.py
2. localhost:1337 will be your app depending on how run.py is started.
3. changes ports as necessary
4. profit
