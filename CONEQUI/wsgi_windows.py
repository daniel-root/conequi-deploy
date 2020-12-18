activate_this = 'C:/Apache24/htdocs/myenv/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/Apache24/htdocs/myenv/Lib/site-packages')




# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Apache24/htdocs/myenv/conequi-deploy')
sys.path.append('C:/Apache24/htdocs/myenv/conequi-deploy/CONEQUI')

os.environ['DJANGO_SETTINGS_MODULE'] = 'CONEQUI.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CONEQUI.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
