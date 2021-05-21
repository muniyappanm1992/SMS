# activate_this = r'C:\Muniyappan\Django\SalemTerminal\IOCLSalem\venv\Scripts\activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
# exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir(r'C:\Muniyappan\Django\SalemTerminal\IOCLSalem\venv\Lib\site-packages')
sys.path.append(r'C:\Muniyappan\Django\SalemTerminal\IOCLSalem')
sys.path.append(r'C:\Muniyappan\Django\SalemTerminal\IOCLSalem/IOCLSalem')
os.environ['DJANGO_SETTINGS_MODULE'] = 'IOCLSalem.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IOCLSalem.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()