from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.HomeView.as_view(), name = 'index'),
    path('contact/<int:pk>', views.ContactDetailView.as_view(), name = "contact")
]