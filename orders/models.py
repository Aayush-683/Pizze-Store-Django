from django.db import models

# Create your models here.
class count(models.Model):
    name = models.CharField(max_length=64)
    count = models.IntegerField()