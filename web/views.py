#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from web.models import Contacts
from django.template import loader
from django.http import Http404

def home(request):

    contact_list = Contacts.objects.all()
    # first_name = ", ".join([contact.first_name for contact in contact_list])
    #return HttpResponse (f"Contacts : {first_name}")
    
    #template = loader.get_template("web/index.html")
    context = {
        'contact_list' : contact_list
        }

    #return HttpResponse(template.render(context, request))

    return render(request, "web/index.html", context)
    

def contact_detail(request, contact_id):
    """ for rendering individual contact page based on contact_id 
    """
    contact = get_object_or_404(Contacts, id = contact_id)
    return render(request, "web/contact_detail.html", {'contact' : contact} )

