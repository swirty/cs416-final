from django.shortcuts import render, redirect
from .models import Post
from CS416FinalProject.forms import UpdateUserForm, CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def homePage(request):
    if isinstance(request.user.id, int):
        context = {'posts': Post.objects.filter(user=request.user).order_by('posted_at').reverse(),
                   'current_user': request.user}
        return render(request, 'cosmos/user-profile.html', context)
    return redirect('/account/login/')

def deliver_css(request):
    print(request.path)
    return render(content_type='css')


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