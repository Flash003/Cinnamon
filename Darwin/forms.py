from django import forms
from .models import *
  
class StoreForm(forms.ModelForm): 
  
    class Meta: 
        model = Store
        fields = ['main_Img'] 