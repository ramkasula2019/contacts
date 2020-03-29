from django.http import HttpResponse
from web.models import Contacts
from django.template import loader

def home(request):

    contact_list = Contacts.objects.all()
    # first_name = ", ".join([contact.first_name for contact in contact_list])
    #return HttpResponse (f"Contacts : {first_name}")
    
    template = loader.get_template("web/index.html")
    context = {
        'contact_list' : contact_list
        }

    return HttpResponse(template.render(context, request))
    

def contact(request, contact_id):
    response = f"the contactid is {contact_id}"
    return HttpResponse (response)