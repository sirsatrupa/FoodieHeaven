from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Feedback, CustContact

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')  

class FeedbackEntry(forms.ModelForm):
    class Meta:
        model=Feedback
        fields = ['username','feedback']


class ContactEntry(forms.ModelForm):
    class Meta:
        model = CustContact
        fields=('cust_name','cust_email','cust_contact','fooditem','help')