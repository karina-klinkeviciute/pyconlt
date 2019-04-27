#!/usr/bin/env python
import os
import sys

from dotenv import load_dotenv, find_dotenv

if __name__ == "__main__":
    load_dotenv(find_dotenv())
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyconlt.settings.pythonanywhere")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
execute_from_command_line(sys.argv)
