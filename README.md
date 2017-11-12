# revolutiontech.ca

[![Build Status](https://travis-ci.org/RevolutionTech/revolutiontech.ca.svg?branch=master)](https://travis-ci.org/RevolutionTech/revolutiontech.ca)
[![codecov](https://codecov.io/gh/RevolutionTech/revolutiontech.ca/branch/master/graph/badge.svg)](https://codecov.io/gh/RevolutionTech/revolutiontech.ca)
[![Updates](https://pyup.io/repos/github/RevolutionTech/revolutiontech.ca/shield.svg)](https://pyup.io/repos/github/RevolutionTech/revolutiontech.ca/)

## Setup

### Prerequisites

revolutiontech.ca requires [memcached](http://memcached.org/), [PostgreSQL](http://www.postgresql.org/), pip and libjpeg-dev, which you can install on debian with:

    sudo apt-get install memcached postgresql postgresql-contrib python-pip python-dev libpq-dev libjpeg-dev

I recommend using a virtual environment for revolutiontech.ca. If you don't have it already, you can install [virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html) and virtualenvwrapper globally with pip:

    sudo pip install virtualenvwrapper

[Update your .profile or .bashrc file](http://virtualenvwrapper.readthedocs.org/en/latest/install.html#shell-startup-file) to create new environment variables for virtualenvwrapper and then create and activate your virtual environment with:

    mkvirtualenv revolutiontech.ca

In the future you can reactivate the virtual environment with:

    workon revolutiontech.ca

### Installation

Then in your virtual environment, you will need to install Python dependencies such as [Gunicorn](http://gunicorn.org/), [Django](https://www.djangoproject.com/), python-memcached, psycopg2, [pillow](https://pillow.readthedocs.org/), django-classbasedsettings,  [sorl-thumbnail](http://sorl-thumbnail.readthedocs.org/), and django-ordered-model. You can do this simply with the command:

    pip install -r requirements.txt

### Configuration

Next we will need to set up some environment variables for your dev instance of revolutiontech.ca. These values should be kept secret. Add a secret key and the database credentials to your `~/.bashrc` file:

    export REVOLUTIONTECH_SECRET_KEY='-3f5yh&(s5%9uigtx^yn=t_woj0@90__fr!t2b*96f5xoyzb%b'
    export REVOLUTIONTECH_DATABASE_URL='postgres://postgres:abc123@localhost:5432/revolutiontech'

For reference, the format of the `DATABASE_URL` is as follows:

    postgres://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}

Of course you should [generate your own secret key](http://stackoverflow.com/a/16630719) and use a more secure password for your database. Also, be sure that special characters (such as `?` and `#`) in your `DATABASE_URL` are percent-encoded. Then source your `~/.bashrc` file to set these environment variables:

    source ~/.bashrc

With everything installed and all files in place, you may now create the database tables. You can do this with:

    python manage.py migrate

### Deployment

In the production environment, you will need to create a directory under `revolutiontech/revolutiontech/settings` called `secrets` and place all of the revolutiontech.ca environment variables in that directory, where the key of the variable is the name of the file and the value of the variable is the content in the file. In addition to the environment variables for the development environment, you will also need to provide one additional environment variable. `REVOLUTIONTECH_ENV` should be set to `PROD`:

    cd revolutiontech/settings
    mkdir secrets
    cd secrets
    echo 'PROD' > REVOLUTIONTECH_ENV

revolutiontech.ca uses Gunicorn with [runit](http://smarden.org/runit/) and [Nginx](http://nginx.org/). You can install them with the following:

    sudo apt-get install runit nginx

Then we need to create the Nginx configuration for revolutiontech.ca:

    cd /etc/nginx/sites-available
    sudo nano revolutiontech.ca

And in this file, generate a configuration similar to the following:

    server {
        server_name revolutiontech.ca;
        return 301 http://www.revolutiontech.ca$request_uri;
    }

    server {
        server_name www.revolutiontech.ca;

        access_log off;

        location /static/ordered_model/ {
            alias /home/lucas/.virtualenvs/revolutiontech.ca/lib/python2.7/site-packages/ordered_model/static/ordered_model/;
        }
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
    exec chpst -e $ROOT/revolutiontech/settings/secrets $GUNICORN -c $ROOT/revolutiontech/gunicorn.py --pid=$PID $APP

Then change the permissions on the file to be executable and symlink the project to /etc/service:

    sudo chmod u+x run
    sudo ln -s /etc/sv/revolutiontech.ca /etc/service/revolutiontech.ca

revolutiontech.ca should now automatically be running on the local machine.
