# activate_this = r'C:\Muniyappan\Django\SalemTerminal\IOCLSalem\venv\Scripts\activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
# exec(open(activate_this).read(),dict(__file__=activate_this))
import os

from django.core.wsgi import get_wsgi_application
# Add the site-packages of the chosen virtualenv to work with
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IOCLSalem.settings')

application = get_wsgi_application()
