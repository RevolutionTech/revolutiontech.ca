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

Then in your virtual environment, you will need to install Python dependencies such as [django](https://www.djangoproject.com/), and [pillow](https://pillow.readthedocs.org/). You can do this simply with the command:

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
