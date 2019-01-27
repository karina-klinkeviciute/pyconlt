Working with docker compose
---------------------------

First make sure you have `docker`_ installed.

pyconlt can be used with `docker_compose`_ to start whole infrastructure of services.

Currently available services:

    - pyconlt_postgres
    - pyconlt_django

Here are some basic commands you can use:

::

    # start everything up (for the first time will create everything) except whats already running.
    docker-compose up (-d for detached mode is available)

    # stop everything (will stop your containers, but it won’t remove them).
    docker-compose stop

    # stop & remove everything (command will stop your containers, but it also removes the stopped containers as well as
    # any networks that were created).
    docker compose down

    # If you want to access the running django app or postgres in a container
    docker exec -it <container-hash> /bin/sh

Note: You do not need to cleanup the image every time. In fact, leaving the old
image will allow to build a new image faster (due to docker caching).

Please take a look at `docker documentation`_ as it has many sub-commands.


.. _docker: https://www.docker.com/
.. _docker_compose: https://docs.docker.com/compose/
.. _docker documentation: https://docs.docker.com/engine/reference/commandline/cli/
