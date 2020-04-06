from django.contrib import admin

# Register your models here.
from .models import Contacts, ContactNumber, Label

admin.site.register(Contacts)
admin.site.register(ContactNumber)
admin.site.register(Label)
