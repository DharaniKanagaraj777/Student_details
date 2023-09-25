from django.db import models

# Create your models here.
class project(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Department = models.CharField(max_length=20)
    Marks = models.IntegerField()