from django.db import models

# Create your models here.


class Label(models.Model):
    ''' A label for multiple contact '''
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30, null=True, blank=True)
    company = models.CharField(max_length=30, null=True, blank=True)
    dob = models.IntegerField()
    label = models.ManyToManyField(Label)
    #number = models.IntegerField()

    def __str__(self):
        return self.first_name


class ContactNumber(models.Model):
    """A contact number for inidividual model

    Arguments:
        models {[type]} -- [description]
    """
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    number = models.IntegerField()
    type = models.CharField(
        max_length=50, default="Primary", null=True, blank=True)

    def __str__(self):
        return f"{self.contact.first_name} {self.number} {self.type}"
