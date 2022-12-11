# @login_required(login_url='login')
# def home_page(request):
#     context = {'posts': Post.objects.filter(user=request.user).order_by('posted_at').reverse()}
#     return render(request, 'cosmos/user-profile.html', context)
#
#
# def user_page(request, user_id):
#     context = {'posts': Post.objects.filter(user_id=user_id).order_by('posted_at').reverse()}
#    return render(request, 'cosmos/user-profile.html', context)
from django.shortcuts import render, redirect
from .models import Post
from CS416FinalProject.forms import UpdateUserForm, CreateUserForm, CreatePostForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def homePage(request):
    context = {'posts': Post.objects.filter(user=request.user).order_by('posted_at').reverse(),
               'current_user': request.user}
    return render(request, 'cosmos/user-profile.html', context)


def showProfile(request, other_user=None):
    if request.method == 'POST' or other_user == request.user.id or other_user is None:
        redirect('/')
    context = {'posts': Post.objects.filter(user=other_user).order_by('posted_at').reverse(),
               'current_user': request.user}
    return render(request, 'cosmos/user-profile.html', context)


@login_required(login_url='login')
def createPost(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            user = request.user
            post_body = form.cleaned_data['post_body']
            post = Post(user=user, post_body=post_body)
            post.save()
            return redirect('/')
    context = {'form': CreatePostForm(),
               'header_flavor': 'Create a Post',
               'button_flavor': 'Go!'}
    return render(request, 'cosmos/create-post.html', context)


@login_required(login_url='login')
def showPost(request, view_post=None):
    if request.method == 'POST' or view_post is None:
        return redirect('/')
    context = {'posts': Post.objects.filter(id=view_post).union(Post.objects.filter(reply_id=view_post)),
               'current_user': request.user}
    return render(request, 'cosmos/post-thread.html', context)

@login_required(login_url='login')
def createReply(request, other_post=None):
    if other_post is None:
        return redirect('landing')
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            user = request.user
            post_body = form.cleaned_data['post_body']
            post = Post(reply_id=other_post, user=user, post_body=post_body)
            post.save()
            return redirect('/')
    context = {'form': CreatePostForm(),
               'header_flavor': 'Create a Post',
               'button_flavor': 'Go!'}
    return render(request, 'cosmos/create-post.html', context)