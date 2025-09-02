from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    image = models.ImageField(upload_to="profile/", null=True, blank=True)

    def __str__(self):
        return self.username