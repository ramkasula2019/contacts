from django.db import models

# Create your models here.

class Contacts(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 30)
    number = models.IntegerField()
    dob = models.IntegerField()

def __str__(self):
    return self.first_name
