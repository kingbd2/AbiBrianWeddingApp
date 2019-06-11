""" Production Settings """

# import os
# import dj_database_url
from .dev import *
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

############
# SECURITY #
############

DEBUG = False

# Set to your Domain here (eg. 'django-vue-template-demo.herokuapp.com')
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = [".abiellaandbriangetmarried.ca", "localhost", "127.0.0.1"]

# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_SSL_REDIRECT = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_HSTS_SECONDS = 60
