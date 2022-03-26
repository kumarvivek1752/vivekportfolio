import email
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        
        fields = ['full_name','email','phone_number','msg']


    def __init__(self,*args,**kwargs):
        super(ContactForm,self).__init__(*args,**kwargs)
        self.fields['full_name'].widget.attrs['placeholder']='Enter First Name'
        self.fields['email'].widget.attrs['placeholder']='Enter Phone Number'
        self.fields['phone_number'].widget.attrs['placeholder']='Enter Phone Number'
        self.fields['msg'].widget.attrs['placeholder']='Enter Message'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'





