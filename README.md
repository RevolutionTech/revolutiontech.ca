# revolutiontech.ca

## Deprecated

This project is no longer being maintained by the owner. The Revolution Technologies website has been moved to a fully static website [hosted on GitHub Pages](https://github.com/RevolutionTech/revolutiontech.github.io).

---

![CI](https://github.com/RevolutionTech/revolutiontech.ca/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/RevolutionTech/revolutiontech.ca/branch/main/graph/badge.svg)](https://codecov.io/gh/RevolutionTech/revolutiontech.ca)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b4326bf2a9d34f8ba5e77e79c0da49c0)](https://www.codacy.com/app/RevolutionTech/revolutiontech.ca)

## Setup

### Installation

Use [poetry](https://github.com/sdispater/poetry) to install Python dependencies:

    poetry install
    
### Configuration

revolutiontech.ca reads in environment variables from your local `.env` file. See `.env-sample` for configuration options. Be sure to [generate your own secret key](http://stackoverflow.com/a/16630719).

With everything installed and all files in place, you may now create the database tables. You can do this with:

    poetry run python manage.py migrate
