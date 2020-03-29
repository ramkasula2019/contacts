#from django.http import HttpResponse
from django.shortcuts import render
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
    try:
        contact = Contacts.objects.get(id = contact_id)
        print(contact)
    except Contacts.DoesNotExist:
        raise Http404 ("Contact page not found")

    contact_dict  = {
        'first_name' : contact.first_name,
        'last_name' : contact.last_name,
        'address' : contact.address,
        'dob' : contact.dob,
        #'number' : [contact_number.number for contact_number in ContactNumber.objects.filter(id= contact_id)]
        'number' :  [contact_number.number for contact_number in contact.contactnumber_set.all()]

        }
    return render(request, "web/contact_detail.html", {'contact_dict':contact_dict})
