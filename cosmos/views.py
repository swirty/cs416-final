# @login_required(login_url='login')
# def home_page(request):
#     context = {'posts': Post.objects.filter(user=request.user).order_by('posted_at').reverse()}
#     return render(request, 'cosmos/user-profile.html', context)
#
#
# def user_page(request, user_id):
#     context = {'posts': Post.objects.filter(user_id=user_id).order_by('posted_at').reverse()}
#    return render(request, 'cosmos/user-profile.html', context)
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from CS416FinalProject.forms import UpdateUserForm, CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

@login_required(login_url='login')
def homePage(request):
    if isinstance(request.user.id, int):
        context = {'posts': Post.objects.filter(user=request.user).order_by('posted_at').reverse(),
                   'current_user': request.user}
        return render(request, 'cosmos/user-profile.html', context)
    return redirect('/account/login/')

@login_required(login_url='login')
def editUser(request):
    if isinstance(request.user.id, int):
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
                return render(request, 'registration/success.html', context={'success_flavor': 'User Edited Successfully'})
        return render(request, 'registration/edit-create-user.html', context)
    return redirect('/account/login/')

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


def showProfile(request, other_user=None):
    if request.method == 'POST' or other_user == request.user.id or other_user is None:
        redirect('/')
    context = {'posts': Post.objects.filter(user=other_user).order_by('posted_at').reverse(),
               'current_user': request.user}
    return render(request, 'cosmos/user-profile.html', context)

@login_required(login_url='login')
def createPost(request):
    return None

@login_required(login_url='login')
def showPost(request):
    return None