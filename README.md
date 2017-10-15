# SimplestFlaskApp

This is simplest flask app created just for practice in pure JavaScript on client side.

Features:
--------

- Pure JavaScript for frontend
- MySQL with basic settings
- Flask-SQLAlchemy with basic simple model
- Easy database migrations with Flask-Migrate
- Flask-WTForms for validation of form
- Unittest for basic app tests
- CSS and JS minification using webpack
- gunicorn and nginx as server

# Getting Started

Preparing Flask modules and Environment Variables
------------------------------------------------

For first clone this repository:

` git clone https://github.com/SandPipper/SimplestFlaskApp `

And install pyvenv:

` sudo apt-get install pyvenv `

Create virtual environment for your project:

` pyvenv-3.5 name_of_your_environment `

Edit activate script in your virtual environment:

`nano name_of_your_environment/bin/activate `


Adding to the end of file your environment variables:

```
export USER="your_mysql_user"
export PASSWORD="your_mysql_password"
export DB_NAME="your_db_name"
export SECRET_KEY="your_secret_key"
```

Activate your virtual environment:

` source name_of_your_environment/bin/activate `

Install python packages from requirements:

` pip install -r requirements.txt `

Install MySQL server and initialize data base
--------------------------------------------

Install MySQL server:

```
sudo apt-get update
sudo apt-get install mysql-server
```


Initialize data base and start migration script:

```
python migrate.py db init
python migrate.py db migrate
python migrate.py db upgrade
```


To run it in werkzeug(native flask server) use `python run.py`

To run it with gunicorn use `gunicorn run:app`


Install and initialize nginx:
----------------------------

Install `sudo apt-get install nginx`


Configure it:

```
sudo rm /etc/nginx/sites-enabled/default
sudo nano /etc/nginx/sites-available/SimplestFlaskApp
```


Put the next with edited by you path to root folder of project:

```
server {
    listen 80;
    server_name 127.0.0.1;

    root /home/path/to/SimplestFlaskApp;

    access_log /home/path/to/SimplestFlaskApp/logs/nginx/access.log;
    error_log /home/path/to/SimplestFlaskApp/logs/nginx/error.log;

    location / {
        proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        if (!-f $request_filename) {
            proxy_pass http://127.0.0.1:5000;
            break;
        }
    }

    location /static {
        alias /home/path/to/SimplestFlaskApp/app/static/;
        autoindex on;
        add_header Cache-Control public;
    }

}
```


Save changes and create directory for logs:

` mkdir -p logs/nginx `


The lasts steps:

```
sudo ln -s /etc/nginx/sites-available/SimplestFlaskApp /etc/nginx/sites-enabled/
sudo nginx -t
```

Now go to `127.0.0.1` and enjoy for this work application.

Unittests
---------
To run unittests execute next in root folder of app:

`python tests.py`

A few word about webpack
------------------------

If you want change `.css` or `.js` files and rebundled it with webpack
install it `npm install webpack` and use ` webpack -p `

If you will have some problem with node.js ` sudo apt-get update && sudo apt-get install nodejs-legacy `
And don't forget install all dependences with ` npm i <package_name> `

