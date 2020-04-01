from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'index'),
    path('<int:pk>', views.ContactDetailView.as_view(), name = "contact")
]