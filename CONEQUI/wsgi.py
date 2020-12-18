"""
WSGI config for CONTEQUI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

#sys.path.append('C:/Apache24/htdocs/myenv/conequi-deploy')
#sys.path.append('C:/Apache24/htdocs/myenv/conequi-deploy/CONEQUI')
#import sys
sys.path.insert(0, 'C:/Apache24/htdocs/myenv/conequi-deploy')

#os.environ['DJANGO_SETTINGS_MODULE'] = 'CONEQUI.settings'
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CONEQUI.settings")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CONEQUI.settings')

application = get_wsgi_application()
