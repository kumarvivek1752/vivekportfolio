
import email
from django.shortcuts import HttpResponse, render

from contact.models import Contact 




def home(request):

    return render(request,'index.html')

def contact_response(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']

        data = Contact(full_name=full_name,email=email,phone=phone,msg=msg)
        data.save()



        print(full_name,email,phone,msg)

    return render(request,"contact_form_response.html")