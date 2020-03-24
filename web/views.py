from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello user, welcome to contact web application")