from django import forms
from .models import My_design

class DesignForm(forms.ModelForm):
    class Meta:
        model = My_design
        fields = ['title', 'description', 'author', 'status']

