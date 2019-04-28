# pyconlt
A repository for a website for PyCon Lithuania.

Deployable on PythonAnywhere.

An app for organizing a conference.

Existing tools:

* Listing speakers.
* CFP submission and management.
* Approving submitted applications. Approved talks are automatically shown on Talks page and approved speakers on Speakers page.
* Program management with slots and option to add talks to slots.

Planned features:

* Having multiple events in one page, e.g. for different years of conference.

## Setting development environment

If you prefer Docker follow instructions in docker-compose.rst.
Docker workflow might save you some time if you are used to Docker.

Alternative workflow:

* Install pipenv (e.g. `pip3 install --user pipenv`) if you don't
  have it yet.

* Install all requires packages `pipenv install`.

* Run pipenv shell `pipenv shell`. I recommend to start using
  direnv (see https://github.com/direnv/direnv) if you are not
  doing it yet. This will run `pipenv shell` command automatically
  for you.

* Install posgresql DB and create pysql database.

* Create /pyconlt/settings/local.py with following content:

```python
import os

from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pyconlt',
    }
}
```

* Run `python manage.py migrate`

* Import data using on of the two methods:

    * `python manage.py loaddata data.json`

    * `psql < pyconlt.dump`

  Ask for data.json or pyconlt.dump from team members.

* Run `python manage.py runserver`

Now you can develop.

## Deployment

Configure your environment properly in file in pyconlt/settings
folder and specify DJANGO_SETTINGS_MODULE in .env file. E.g.:

```
DJANGO_SETTINGS_MODULE=pyconlt.settings.pythonanywhere
```

Follow deployment instructions for your platform. For
pythonanywhere we have deploy.sh script in the system.
