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
# ALLOWED_HOSTS = ['0.0.0.0', 'localhost', 'talentedapp.herokuapp.com', '.herokuapp.com']
ALLOWED_HOSTS = [".abiellaandbriangetmarried.ca", "localhost", "127.0.0.1"]

SECURE_CONTENT_TYPE_NOSNIFF = True

# ?: (security.W004) You have not set a value for the SECURE_HSTS_SECONDS setting. If your entire site is served only over SSL, you may want to consider setting a value and enabling HTTP Strict Transport Security. Be sure to read the documentation first
# enabling HSTS carelessly can cause serious, irreversible problems.
# ?: (security.W006) Your SECURE_CONTENT_TYPE_NOSNIFF setting is not set to True, so your pages will not be served with an 'X-Content-Type-Options: nosniff' header. You should consider enabling this header to prevent the browser from identifying content types incorrectly.
# ?: (security.W007) Your SECURE_BROWSER_XSS_FILTER setting is not set to True, so your pages will not be served with an 'X-XSS-Protection: 1; mode=block' header. You should consider enabling this header to activate the browser's XSS filtering and help prevent XSS attacks.
# ?: (security.W008) Your SECURE_SSL_REDIRECT setting is not set to True. Unless your site should be available over both SSL and non-SSL connections, you may want to either set this setting True or configure a load balancer or reverse-proxy server to redirect all connections to HTTPS.
# ?: (security.W012) SESSION_COOKIE_SECURE is not set to True. Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
# ?: (security.W016) You have 'django.middleware.csrf.CsrfViewMiddleware' in your MIDDLEWARE, but you have not set CSRF_COOKIE_SECURE to True. Using a secure-only CSRF cookie makes it more difficult for network traffic sniffers to steal the CSRF token.
# ?: (security.W018) You should not have DEBUG set to True in deployment.
# ?: (security.W019) You have 'django.middleware.clickjacking.XFrameOptionsMiddleware' in your MIDDLEWARE, but X_FRAME_OPTIONS is not set to 'DENY'. The default is 'SAMEORIGIN', but unless there is a good reason for your site to serve other parts of itself in a frame, you should change it to 'DENY'.
