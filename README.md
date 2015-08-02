# revolutiontech.ca
### Created by: Lucas Connors

## Setup

### Prerequisites

revolutiontech.ca requires [PostgreSQL](http://www.postgresql.org/), which you can install on debian with:

    sudo apt-get install postgresql postgresql-contrib libpq-dev python-dev

I recommend using a virtual environment for revolutiontech.ca. If you don't have it already, you can install [virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html) and virtualenvwrapper globally with pip:

    sudo pip install virtualenv virtualenvwrapper

[Update your .profile or .bashrc file](http://virtualenvwrapper.readthedocs.org/en/latest/install.html#shell-startup-file) to create new environment variables for virtualenvwrapper and then create and activate your virtual environment with:

    mkvirtualenv revolutiontech.ca

In the future you can reactivate the virtual environment with:

    workon revolutiontech.ca

### Installation

Then in your virtual environment, you will need to install Python dependencies such as [Gunicorn](http://gunicorn.org/), [django](https://www.djangoproject.com/), psycopg2, and [pillow](https://pillow.readthedocs.org/). You can do this simply with the command:

    pip install -r requirements.txt

### Configuration

Next we will need to create a file in the same directory as `settings.py` called `settings_secret.py`. This is where we will store all of the settings that are specific to your instance of revolutiontech.ca. Most of these settings should be only known to you. Your file should define a secret key, and the database credentials. Your `settings_secret.py` file might look something like:

    SECRET_KEY = '-3f5yh&(s5%9uigtx^yn=t_woj0@90__fr!t2b*96f5xoyzb%b'
    DATABASE_USER = 'postgres'
    DATABASE_PASSWORD = 'abc123'
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = '5432'

Of course you should [generate your own secret key](http://stackoverflow.com/a/16630719) and use a more secure password for your database.

With everything installed and all files in place, you may now create the database tables. You can do this with:

    python manage.py migrate

### Deployment

First you will want to manually change some settings in `settings.py` for production. You should update DEBUG and ALLOWED_HOSTS to look like the following:

    DEBUG = False
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost',]

revolutiontech.ca uses Gunicorn with [runit](http://smarden.org/runit/) and [Nginx](http://nginx.org/). You can install them with the following:

    sudo apt-get install runit nginx

Then we need to create the Nginx configuration for revolutiontech.ca:

    cd /etc/nginx/sites-available
    sudo nano revolutiontech.ca

And in this file, generate a configuration similar to the following:

    server {
        server_name www.revolutiontech.ca;
        return 301 http://revolutiontech.ca$request_url;
    }

    server {
        server_name revolutiontech.ca;

        access_log off;

        location /static/admin/ {
            alias /home/lucas/.virtualenvs/revolutiontech.ca/lib/python2.7/site-packages/django/contrib/admin/static/admin/;
        }
        location /static/ {
            alias /home/lucas/revolutiontech.ca/static/;
        }
        location /media/ {
            alias /home/lucas/revolutiontech.ca/media/;
        }

        location /favicon.ico {
            alias /home/lucas/revolutiontech.ca/static/favicon.ico;
        }

        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header X-Forwarded-Host $server_name;
            proxy_set_header X-Real-IP $remote_addr;
            add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
        }
    }

Save the file and link to it from sites-enabled:

    cd ../sites-enabled
    sudo ln -s ../sites-available/revolutiontech.ca revolutiontech.ca

Then we need to create a script to run revolutiontech.ca on boot with runit:

    sudo mkdir /etc/sv/revolutiontech.ca
    cd /etc/sv/revolutiontech.ca
    sudo nano run

In this file, create a script similar to the following:

    #!/bin/sh

    GUNICORN=/home/lucas/.virtualenvs/revolutiontech.ca/bin/gunicorn
    ROOT=/home/lucas/revolutiontech.ca/revolutiontech
    PID=/var/run/gunicorn.pid

    APP=revolutiontech.wsgi:application

    if [ -f $PID ]; then rm $PID; fi

    cd $ROOT
    exec $GUNICORN -c $ROOT/revolutiontech/gunicorn.py --pid=$PID $APP

Then change the permissions on the file to be executable and symlink the project to /etc/service:

    sudo chmod u+x run
    sudo ln -s /etc/sv/revolutiontech.ca /etc/service/revolutiontech.ca

revolutiontech.ca should now automatically be running on the local machine.
