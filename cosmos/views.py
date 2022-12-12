# @login_required(login_url='login')
# def home_page(request):
#     context = {'posts': Post.objects.filter(user=request.user).order_by('posted_at').reverse()}
#     return render(request, 'cosmos/user-profile.html', context)
#
#
# def user_page(request, user_id):
#     context = {'posts': Post.objects.filter(user_id=user_id).order_by('posted_at').reverse()}
#    return render(request, 'cosmos/user-profile.html', context)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreatePostForm
from .models import Post, Reaction, User

@login_required(login_url='login')
def homePage(request):
    context = {'posts': Post.objects.filter(user=request.user).order_by('posted_at').reverse(),
               'current_user': request.user}
    return render(request, 'cosmos/user-profile.html', context)

@login_required(login_url='login')
def showProfile(request, other_user=None):
    if request.method == 'POST' or other_user == request.user.id or other_user is None:
        return redirect('landing')
    get_object_or_404(User, id=other_user)

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
    get_object_or_404(Post, id=view_post)

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

# the worst function in the entire project
@login_required(login_url='login')
def reactionAJAXOperations(request):
    def likeReturn(postID):
        return HttpResponse(Reaction.objects.filter(reaction='LIKE', post_id=postID).count())

    def dislikeReturn(postID):
        return HttpResponse(Reaction.objects.filter(reaction='DISLIKE', post_id=postID).count())

    if request.method == 'GET':
        return redirect('landing')

    # setter db operations
    if request.POST['operation'] == 'SET':
        # get the reaction associated with this post and user
        react = Reaction.objects.filter(reaction=request.POST['goal'], post_id=request.POST['postID'], user_id=request.POST['userID'])
        # is there a reaction of type 'target' between this user and this post?
        if react.count() == 0:
            # no, create one, old QueryList in react can be clobbered
            react = Reaction(reaction=request.POST['goal'], post_id=request.POST['postID'], user_id=request.POST['userID'])
            react.save()
        else:
            # yes, delete it
            react[0].delete()

    #getter db operations
    if request.POST['goal'] == 'LIKE':
        return likeReturn(request.POST['postID'])

    if request.POST['goal'] == 'DISLIKE':
        return dislikeReturn(request.POST['postID'])
