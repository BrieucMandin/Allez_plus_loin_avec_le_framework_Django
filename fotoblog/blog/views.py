from django.shortcuts import render
from django.contrib.auth.decorators import login_required   
# Create your views here.

@login_required
def home(request):
    print("Utilisateur connecté :", request.user.is_authenticated)
    return render(request, 'blog/home.html')