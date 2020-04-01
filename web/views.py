#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from web.models import Contacts
from django.views.generic import ListView, DetailView

class HomeView(ListView):
    model = Contacts
    context_object_name = "contacts"
    template_name = "web/index.html"

class ContactDetailView(DetailView):
    model = Contacts
    context_object_name = "contact"
    template_name = "web/contact_detail.html"


