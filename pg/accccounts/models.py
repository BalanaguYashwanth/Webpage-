from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userprofile(models.Model):
    pg_id=models.IntegerField()
