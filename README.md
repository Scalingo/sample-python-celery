Sample Crystal application
======================================

Running Locally
---------------

First, you need to have a working python installation :

https://wiki.python.org/moin/BeginnersGuide/Download

Next you'll need a working virtualenv installation :
```sh
pip install virtualenv
```

### Install dependencies

```
virtualenv
. bin/activate
pip install -r requirements.txt
```

### Running
This application is composed of two container:
  * The celery server which take tasks and return result
  * The flask server which run the webserver that send tasks to the celery server and display results
  * A redis server

#### Communication with redis

You will need a working redis server.
See http://redis.io/download

Or with docker :
```sh
docker run -p 6379:6379 -d redis
```
And export your redis url in an environment variable :
```sh
export REDIS_URL=redis://
```
#### Running with foreman
If you have foreman installed on your system you can launch the web server using :
```sh
foreman start
```

#### Running manually
If you don't have foreman installed you'll have to launch the two component manually :

##### Start the celery server
```sh
celery worker --app=scal_task.app
```

##### Stat the web server
```sh
python app.py
```

The application will be avilable on http://localhost:5000

Deploying on Scalingo
---------------------

Create an application on https://scalingo.com with a redis addon, then:

```
git remote add scalingo git@scalingo.com:<name_of_your_app>.git
git push scalingo master
```

By default scalingo only launch your web container. To launch your worker container, you'll need to go to your dashboard and set your worker container amount to 1.


And that's it!

The application is running at this url: https://sample-python-celery.scalingo.io

Deploy in one click
-------------------

[![Deploy to Scalingo](https://cdn.scalingo.com/deploy/button.svg)](https://my.scalingo.com/deploy)

Links
-----
http://www.celeryproject.org/
http://redis.io/
http://flask.pocoo.org/
