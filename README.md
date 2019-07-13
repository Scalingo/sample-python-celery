# Sample Python/Celery application

## Running Locally

```sh
$ docker-compose up
```

### Running

This application is composed of three containers:
  * The Celery server which takes tasks and return result
  * The Flask server which runs the webserver that sends tasks to the Celery server and display results
  * A Redis server

The application will be available on http://localhost:3000

## Deploying on Scalingo

Create an application on https://scalingo.com with a Redis addon, then:

```
git remote add scalingo git@scalingo.com:<name_of_your_app>.git
git push scalingo master
```

By default Scalingo only launches your web container. To launch your worker container, you'll need to go to your dashboard and set your worker container amount to 1.

And that's it!

The application is running at this URL: https://sample-python-celery.scalingo.io

## Deploy in one click

[![Deploy to Scalingo](https://cdn.scalingo.com/deploy/button.svg)](https://my.osc-fr1.scalingo.com/deploy)

## Links

http://www.celeryproject.org
https://Redis.io
http://flask.pocoo.org
