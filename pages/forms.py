from django import forms
from .models import My_design, Contact


class DesignForm(forms.ModelForm):
    class Meta:
        model = My_design
        fields = ['title', 'description', 'author', 'status']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'msg']