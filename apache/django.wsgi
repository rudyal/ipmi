import os, sys
sys.path.append('/var/www/django')
sys.path.append('/var/www/django/idaho')
os.environ['DJANGO_SETTINGS_MODULE'] = 'idaho.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()