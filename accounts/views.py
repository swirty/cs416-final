from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def register_view(request):
    user_creation_form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if user_creation_form.is_valid():
            user_creation_form.save()
            return redirect('landing')
    return render(request, 'cosmos/register.html', {'form': user_creation_form})

def login_view(request):
    auth_form = AuthenticationForm(data=(request.POST or None))
    if request.method == 'POST':
        if auth_form.is_valid():
            user_credentials = auth_form.get_user()
            login(request, user_credentials)
            return redirect('landing')
    return render(request, 'cosmos/login.html', {'form': auth_form})