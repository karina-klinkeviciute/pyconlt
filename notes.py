# get pyconlt/settings/local.py
# rename to json
python manage.py migrate --settings=pyconlt.settings.local
python manage.py loaddata pycon_database.json --settings=pyconlt.settings.local
python manage.py runserver --settings=pyconlt.settings.local
python manage.py createsuperuser --settings=pyconlt.settings.local
