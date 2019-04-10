Working with pytest
-------------------

First make sure you have pyconlt database setup and a user created in it:

- Create a pyconlt DB:
    - For this check README.md
- Create superuser for it:
    - In psql: CREATE ROLE pyconlt SUPERUSER;
    - Then: GRANT ALL PRIVILEGES ON DATABASE pyconlt TO pyconlt;
    - And then: ALTER ROLE "pyconlt" WITH LOGIN;

If the DB and the user created successfully just run:

    pytest or python -m pytest in pipenv shell
    for specific test file just add the path: pytest path/to/test/test_smth.py
    (-s if an actual print() statement needs to be printed out in the terminal)
