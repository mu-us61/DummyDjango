from django.db import models
from django.contrib.auth import hashers

# Create your models here.


class MyUser(models.Model):
    username = models.CharField(max_length=200, unique=True, blank=False, null=False)
    hashed_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.hashed_password = hashers.make_password(raw_password)

    def check_password(self, raw_password):
        return hashers.check_password(raw_password, self.hashed_password)
