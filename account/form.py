from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.forms.widgets import PasswordInput , TextInput
from .models import MyUser

class CreateUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ["username", "email", "phone_number", "address", "password1", "password2"]
        
class LoginForm (AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)