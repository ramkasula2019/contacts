from django.db import models

# Create your models here.

class Contacts(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 30)
    #number = models.IntegerField()
    dob = models.IntegerField()

    def __str__(self):
        return self.first_name


class ContactNumber(models.Model):
    """A contact number for inidividual model
    
    Arguments:
        models {[type]} -- [description]
    """
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    number = models.IntegerField()
    type = models.CharField(max_length=50,default="Primary", null=True, blank=True)

    def __str__(self):
        return f"{self.contact.first_name} {self.number} {self.type}" 