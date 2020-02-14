from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password'}))
    username.widget.attrs.update({'class': 'username'})


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=180, required=True)
    last_name = forms.CharField(max_length=70, required=True)
    email = forms.EmailField(max_length=254, help_text='enter a valid mail address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')