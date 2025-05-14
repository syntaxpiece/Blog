from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'user',
            'class': 'input',
            'placeholder': '',  
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'id': 'email',
            'class': 'input',
            'placeholder': '',
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'pass1',
            'class': 'input',
            'data-type': 'password',
            'placeholder': '',
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'pass2',
            'class': 'input',
            'data-type': 'password',
            'placeholder': '',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class SigninForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'user',
            'class': 'input',
            'placeholder': '',
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'pass1',
            'class': 'input',
            'data-type': 'password',
            'placeholder': '',
        })
    )