from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.home, name = 'index'),
    path('contact/<int:contact_id>', views.contact_detail, name = "contact")
]