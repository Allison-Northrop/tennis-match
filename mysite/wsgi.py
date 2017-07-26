"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
os.environ["SECRET_KEY"] = 'tv8rn9m5y7@#q%n@vu6kxvrz+go&+79y+_#*%9qx8#2qw%p+ww'

os.environ["SOCIAL_AUTH_TWITTER_KEY"] = 'TGyJSOCXh4Z0pDVpf6fNzgeff'

application = get_wsgi_application()
