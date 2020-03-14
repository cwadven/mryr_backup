from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class Profile(AbstractUser):
#     Phone = models.CharField(max_length=13, null=True) #전화번호
#     Credit = models.FloatField(null=True) #전화번호

#     def __str__(self):
#         return '%s' % (self.username)