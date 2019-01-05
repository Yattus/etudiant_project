"""
WSGI config for etudiant_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append("/home/alex/Code/etudiant/etudiant_project/")

os.environ["DJANGO_SETTINGS_MODULE"] = "etudiant_project.settings"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'etudiant_project.settings')

application = get_wsgi_application()
