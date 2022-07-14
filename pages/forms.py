from django import forms
from .models import My_design

class NewDesignForm(forms.ModelForm):
    class Meta:
        model = My_design
        fields = ['title', 'description', 'author', 'status']

