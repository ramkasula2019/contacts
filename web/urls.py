from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.home, name = 'index'),
    path('contact/<int:contact_id>', views.contact, name = "contact")
]