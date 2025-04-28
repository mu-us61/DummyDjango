import os, django, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DummyDjango.settings")  # Replace 'myproject' with your project name
django.setup()

from AppBase.models import Article

article = Article.objects.all()

print(article[:1])
