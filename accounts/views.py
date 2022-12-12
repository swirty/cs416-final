from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import UpdateUserForm, CreateUserForm


# IMPORTANT NOTE ABOUT LOGIN AND 'login.html': Django will automagically look in templates/registration/ for login.html!


@login_required(login_url='login')
def editUser(request):
        form = UpdateUserForm(request.POST, instance=request.user or None)
        context = {'current_user': request.user,
                   'form': form,
                   'header_flavor': 'Update Your Account',
                   'button_flavor': 'Save Changes'}
        if request.method == 'POST':
            if form.is_valid():
                username = form.cleaned_data['username']
                password_hash = make_password(form.cleaned_data['password'])
                user = User(username=username, password=password_hash, id=request.user.id)
                user.save()
                return render(request, 'registration/success.html',
                              context={'success_flavor': 'User Edited Successfully'})
        return render(request, 'registration/edit-create-user.html', context)


def createUser(request):
    if isinstance(request.user.id, int):
        return redirect('/')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password_hash = make_password(form.cleaned_data['password'])
            user = User(username=username, password=password_hash)
            user.save()
            return render(request, 'registration/success.html', context={'success_flavor': 'User Created Successfully'})
    context = {'form': CreateUserForm(),
               'header_flavor': 'Create Your Account',
               'button_flavor': 'Create Account'}
    return render(request, 'registration/edit-create-user.html', context)


# def register_view(request):
#     user_creation_form = UserCreationForm(request.POST or None)
#     if request.method == 'POST':
#         if user_creation_form.is_valid():
#             user_creation_form.save()
#             return redirect('landing')
#     return render(request, 'cosmos/register.html', {'form': user_creation_form})
#
# def login_view(request):
#     auth_form = AuthenticationForm(data=(request.POST or None))
#     if request.method == 'POST':
#         if auth_form.is_valid():
#             user_credentials = auth_form.get_user()
#             login(request, user_credentials)
#             return redirect('landing')
#     return render(request, 'cosmos/login.html', {'form': auth_form})