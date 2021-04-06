from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'first_name'}
    ), required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'last_name'}
    ), required=True, max_length=50)
    username = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'username'}
    ), required=True, max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'name': 'email'}
    ), required=True, max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'name': 'password1'}
    ), required=True, max_length=50)
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'name': 'password2'}
    ), required=True, max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
