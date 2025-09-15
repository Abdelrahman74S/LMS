from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm ,UserChangeForm
from django.forms.widgets import PasswordInput , TextInput
from .models import MyUser

class CreateUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ["username", "email", "MyPhoto","phone_number", "address", "account_type"]

class changeprofile(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ["username", "email", "MyPhoto","phone_number", "address"]

class LoginForm (AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)