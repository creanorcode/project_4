#!/usr/bin/env python
# This shebang line allows the script to be run as an executable.
import os   # Import operating system utilities.
import sys  # Import system-specific parameters and functions.


def main():
    # Set the default Django settings module for the 'manage.py' script.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_4.settings')
    try:
        # Attempt to import and execute Django´s command-line utility.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If Django is not installed or available, raise a clear error.
        raise ImportError(
            "Couldn´t import Django. Are you sure it´s \
            installed and available on your PYTHONPATH"
            "Did you forget to activate a virtual environment?"
            ) from exc
    # Execute the command-line utility with the arguments provided.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
