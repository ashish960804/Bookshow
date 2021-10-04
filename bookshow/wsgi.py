"""
WSGI config for bookshow project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookshow.settings')
application = StaticFilesHandler(get_wsgi_application())

application = get_wsgi_application()