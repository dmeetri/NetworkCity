from django.db import models
from django.contrib.auth.models import AbstractUser

from groups.models import *
from educations.models import *

class Users(AbstractUser):
    image = models.ImageField(upload_to="profile/", null=True, blank=True)

    def __str__(self):
        return self.username
    
class Students(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
    birth_date = models.DateField(verbose_name="Дата рождения")
    address = models.TextField(max_length=200)
    phone_number = models.IntegerField(max_length=12)

class Teachers(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    teaching_subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
