from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    select1_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='selected1_users', blank=True)
    select1_content = models.CharField(max_length=20)
    select2_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='selected2_users', blank=True)
    select2_content = models.CharField(max_length=20)
