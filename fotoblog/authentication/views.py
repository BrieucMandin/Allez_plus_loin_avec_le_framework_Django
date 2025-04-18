from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.views.generic import View

from authentication.forms import LoginForm
from authentication.forms import ChangePasswordForm
from authentication.forms import SignupForm
from authentication.forms import UploadProfilePhotoForm


from django.contrib.auth import login
from django.conf import settings

from . import forms
# Create your views here.

class LoginPage(View):
    form_class = forms.LoginForm
    templates_name = 'authentication/login.html'
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, 'authentication/login.html', context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})
    
class LogoutPage(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    

class PasswordChangeView(View):
    message = 'Veuillez saisir les champs suivants pour changer votre mot de passe.'
    form_class = forms.ChangePasswordForm
    def get(self, request):
        form = self.form_class(user=request.user)
        return render(request, 'authentication/password_change.html', context={'form': form, 'message': self.message})
    
    def post(self, request):
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            message = 'Mot de passe changé avec succès.'
            return render(request, 'authentication/password_change_done.html', context={'message': message})
        else:
            message = 'L\'un des champ est incorect'
            return render(request, 'authentication/password_change.html', context={'form': form, 'message': message})



class PasswordChangeDoneView():

    def get(self, request):
        return render(request, 'authentication/password_change_done.html')
    

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render (request, 'authentication/signup.html', context={'form': form})

def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'authentication/upload_profile_photo.html', context={'form': form})

