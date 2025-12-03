from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model=UserSignup
        fields='__all__'
        
class NotesForm(forms.ModelForm):
    class Meta:
        model=Mynotes
        fields=["title","desc","files","cate"]
        
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'