from django import forms


class LogiForm(forms.Form):
    username = forms.CharField(label='Username',max_length=63)
    password = forms.CharField(label='Password',max_length=63,)
    