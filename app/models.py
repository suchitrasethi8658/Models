from enum import unique
from django.db import models

# Create your models here.
class Topics(models.Model):
    topicname=models.CharField(max_length=100,unique=True)
class Webpages(models.Model):
    topicname=models.ForeignKey(Topics,on_delete=models.CASCADE)
    url=models.URLField()
    name=models.CharField(max_length=100)
class AccessRecords(models.Model):
    name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    date=models.DateField()