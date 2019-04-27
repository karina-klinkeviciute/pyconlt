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
Docker workflow might save you some time.

Alternative workflow:

* Install pipenv (e.g. `pip3 install --user pipenv`).

* Install all requires packages `pipenv install`.

* Run pipenv shell `pipenv shell`.

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

* Export DJANGO_SETTINGS_MODULE:

```
export DJANGO_SETTINGS_MODULE=pyconlt.settings.local
```

* Run `python manage.py migrate`

* Import data `python manage.py loaddata data.json` - ask for
  data.json from team members.

* Run `python manage.py runserver`

Now you can develop.
