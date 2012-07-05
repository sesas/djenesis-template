"""
WSGI config for this project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import sys
import os
import imp
from django.core.handlers.wsgi import WSGIHandler

# assume 'apps' is a directory with same parent directory as us 
TOP_DIR = os.path.dirname(os.path.abspath(__file__))
APPS_DIR = os.path.join(TOP_DIR, 'apps')
if APPS_DIR not in sys.path:
    sys.path.insert(0, APPS_DIR)

# assume that the virtualenv is a directory named 'env' that is a sibling to TOP_DIR
ENV_DIR = os.path.join(os.path.dirname(TOP_DIR), 'env')

# if virtualenv exists, activate it
activate_this = os.path.join(ENV_DIR, 'bin', 'activate_this.py')
if os.path.exists(activate_this):
    execfile(activate_this, dict(__file__=activate_this))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)