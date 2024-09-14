
# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class QueryForm(forms.Form):
    query = forms.CharField(label='Query', max_length=100)

class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')