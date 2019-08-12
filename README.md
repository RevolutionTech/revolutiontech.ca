# revolutiontech.ca

[![Build Status](https://travis-ci.org/RevolutionTech/revolutiontech.ca.svg?branch=master)](https://travis-ci.org/RevolutionTech/revolutiontech.ca)
[![codecov](https://codecov.io/gh/RevolutionTech/revolutiontech.ca/branch/master/graph/badge.svg)](https://codecov.io/gh/RevolutionTech/revolutiontech.ca)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b4326bf2a9d34f8ba5e77e79c0da49c0)](https://www.codacy.com/app/RevolutionTech/revolutiontech.ca)

## Setup

### Installation

Use [poetry](https://github.com/sdispater/poetry) to install Python dependencies:

    poetry install
    
### Configuration

revolutiontech.ca uses [python-dotenv](https://github.com/theskumar/python-dotenv) to read environment variables in from your local `.env` file. See `.env-sample` for configuration options. Be sure to [generate your own secret key](http://stackoverflow.com/a/16630719).

With everything installed and all files in place, you may now create the database tables. You can do this with:

    poetry run python manage.py migrate

### Deployment

Deployments are done using `zappa`. First, you will need to decrypt the `zappa_settings.json.enc` to `zappa_settings.json`:

    openssl aes-256-cbc -k $DECRYPT_PASSWORD -in zappa_settings.json.enc -out zappa_settings.json -d

where `$DECRYPT_PASSWORD` contains the key that the settings were encrypted with. Then, use `zappa` to deploy to the production environment:

    poetry run zappa deploy

Once deployed, you will need to set environment variables on the generated Lambda. See `prod.py` for additional environment variables used in production.

Then to publish static assets, run the `manage.py collectstatic` command locally, setting the environment variables for AWS credentials to the values used in production:

    STAGE=production REVOLUTIONTECH_AWS_ACCESS_KEY_ID=1234 REVOLUTIONTECH_AWS_SECRET_ACCESS_KEY=abc123 poetry run python manage.py collectstatic --noinput

You may also need to update `ALLOWED_HOSTS` in `settings/prod.py` to match the assigned URL for the Lambda. Once completed, the assigned URL should be running revolutiontech.ca.

If any changes to `zappa_settings.json` are made, the file should be re-encrypted before being committed. The following bash functions may be helpful for encrypting/decrypting:

    function encrypt_openssl () { openssl aes-256-cbc -k $DECRYPT_PASSWORD -in "$1" -out "$1".enc; }
    function decrypt_openssl () { openssl aes-256-cbc -k $DECRYPT_PASSWORD -in "$1".enc -out "$1" -d; }
