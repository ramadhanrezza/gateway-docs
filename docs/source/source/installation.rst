Installation
************

Gateway Service
===============

Clone the repo::

 git clone https://rezzaramadhan@dev.azure.com/rezzaramadhan/GatewayService/_git/GatewayService

Go to project directory::

 cd /<path>/<to>/<dir>/GatewayService

run composer install::

 composer install

migrate database::

 php artisan migrate:fresh

setup .env file::

 cp .env.example .env
 vim .env

Put these code to your env file::

 APP_NAME=Lumen
 APP_ENV=local
 APP_KEY=<Your-Generated-Key>
 APP_DEBUG=true
 APP_URL=http://localhost
 APP_TIMEZONE=Asia/Jakarta

 LOG_CHANNEL=daily
 LOG_SLACK_WEBHOOK_URL=
 LOG_PATH=/path/to/your/log/services.log

 DB_CONNECTION=pgsql
 DB_HOST=127.0.0.1
 DB_PORT=5432
 DB_DATABASE=<dbname>
 DB_USERNAME=<dbuser>
 DB_PASSWORD=<dbpass>

 CACHE_DRIVER=redis
 QUEUE_DRIVER=redis

 REDIS_HOST=<redis-host>
 REDIS_PORT=<redis-port
 REDIS_DATABASE=0

 JWT_SECRET=<your-jwt-secret>

setup services.yml file::

 cp services.yml.example services.yml
 vim services.yml

For start, put these code on your services.yml file::

 face:
  serviceName: 'Face Microservice'
  uri: 'http://localhost'
  port: 8001
  controllers: {
   face: { 
    name: 'core face', 
    path: face, 
    resource_name: face_face, 
    actions: [{ 
     name: 'list face', 
     path: 'uri:service:controller', 
     operation: list, 
     method: get 
    }]
   }
  }

run your localhost server::

 php -S localhost:8000 -t public

Your Gateway Service are ready to use with some predefined accounts. Try out these curl request to get account credentials::

 curl --location --request POST 'http://localhost:8000/api/auth/login' --form 'username=admin' --form 'password=Sementara123!'

Face Service
============

Dashboard
=========

.. toctree::
   :includehidden:
   :maxdepth: 5