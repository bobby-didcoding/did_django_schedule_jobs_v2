
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.contrib.auth.models import User
from django import forms
 
 
 
 
class UserForm(UserCreationForm):
    '''
    Form that uses built-in UserCreationForm to handle user creation
    '''
    username = forms.EmailField(max_length=254, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Email..'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': '*Password..',}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': '*Confirm Password..',}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
 
 
 
 
class AuthForm(AuthenticationForm):
    '''
    Form that uses built-in AuthenticationForm to handle user auth
    '''
    username = forms.EmailField(max_length=254, required=True,
        widget=forms.TextInput(attrs={'placeholder': '*Email..',}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Password..',}))
 
    class Meta:
        model = User
        fields = ('username','password', )
 
