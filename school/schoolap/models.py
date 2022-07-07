from django.db import models

# Create your models here.
class Database1(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(unique=True)
    registration = models.IntegerField()
    department = models.CharField(max_length=80)
