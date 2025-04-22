from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField()
    description = models.TextField()

    def __str__(self):
        return self.title or "Untitled Article"
