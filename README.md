# revolutiontech.ca

[![Build Status](https://travis-ci.org/RevolutionTech/revolutiontech.ca.svg?branch=master)](https://travis-ci.org/RevolutionTech/revolutiontech.ca)
[![codecov](https://codecov.io/gh/RevolutionTech/revolutiontech.ca/branch/master/graph/badge.svg)](https://codecov.io/gh/RevolutionTech/revolutiontech.ca)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b4326bf2a9d34f8ba5e77e79c0da49c0)](https://www.codacy.com/app/RevolutionTech/revolutiontech.ca)
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

Then in your virtual environment, you will need to install Python dependencies such as [Zappa](https://www.zappa.io/), [Django](https://www.djangoproject.com/), python-memcached, psycopg2, [pillow](https://pillow.readthedocs.org/), django-classbasedsettings, [sorl-thumbnail](http://sorl-thumbnail.readthedocs.org/), and django-ordered-model. You can do this simply with the command:

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

Deployments are done using `zappa`. First, you will need to decrypt the `zappa_settings.json.enc` to `zappa_settings.json`:

    openssl aes-256-cbc -k $DECRYPT_PASSWORD -in zappa_settings.json.enc -out zappa_settings.json -d

where `$DECRYPT_PASSWORD` contains the key that the settings were encrypted with. Then, use `zappa` to deploy to the production environment:

    zappa deploy

Once deployed, you will need to set environment variables on the generated Lambda. In addition to the environment variables for the development environment, you will also need to provide two additional environment variables: `REVOLUTIONTECH_AWS_ACCESS_KEY_ID` and `REVOLUTIONTECH_AWS_SECRET_ACCESS_KEY`.

Then to publish static assets, run the `manage.py collectstatic` command locally, using the production environment variables listed above:

    STAGE=production REVOLUTIONTECH_AWS_ACCESS_KEY_ID=1234 REVOLUTIONTECH_AWS_SECRET_ACCESS_KEY=abc123 python manage.py collectstatic --noinput

You may also need to update `ALLOWED_HOSTS` in `settings/prod.py` to match the assigned URL for the Lambda. Once completed, the assigned URL should be running revolutiontech.ca.

If any changes to `zappa_settings.json` are made, the file should be re-encrypted before being committed. The following bash functions may be helpful for encrypting/decrypting:

    function encrypt_openssl () { openssl aes-256-cbc -k $DECRYPT_PASSWORD -in "$1" -out "$1".enc; }
    function decrypt_openssl () { openssl aes-256-cbc -k $DECRYPT_PASSWORD -in "$1".enc -out "$1" -d; }
