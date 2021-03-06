"""
WSGI config for face project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
import status
from django.core.wsgi import get_wsgi_application

application = WhiteNoise(status, root='static')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'face.settings')

application = get_wsgi_application()
