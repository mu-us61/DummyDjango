# populate_articles.py

import os, sys
import django
from faker import Faker

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DummyDjango.settings")  # Replace 'myproject' with your project name
django.setup()

from AppBase.models import Article  # Replace 'myapp' with your app name

# Initialize Faker
fake = Faker()

# Create 100 articles with random titles and descriptions
for _ in range(100):
    Article.objects.create(
        title=fake.sentence(nb_words=5),  # Random title with 5 words
        description=fake.paragraph(nb_sentences=3),  # Random description with 3 sentences
    )

print("Successfully created 100 articles!")
