#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ


def main():
    """Run administrative tasks."""

    env = environ.Env()

    ROOT_DIR = environ.Path(__file__) - 1

    READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)

    if READ_DOT_ENV_FILE:
        # OS environment variables take precedence over variables from .env
        env.read_env(str(ROOT_DIR.path('.env')))

    ENV = 'smart_work.settings.' + env('ENV')

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", ENV)
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
