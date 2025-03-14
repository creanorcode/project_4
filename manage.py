#!/usr/bin/env python
import os
import sys

if __name__ == '__mail__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_4.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn´t import Django.") from exc
    execute_from_command_line(sys.argv)
