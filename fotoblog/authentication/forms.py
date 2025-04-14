from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=63)
    password = forms.CharField(label='Password',max_length=63,widget=forms.PasswordInput)


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='Old Password',max_length=63,widget=forms.PasswordInput)
    new_password = forms.CharField(label='New Password',max_length=63,widget=forms.PasswordInput)
    new_password_confirm = forms.CharField(label='Confirm New Password',max_length=63,widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('username','email','first_name','last_name','role')