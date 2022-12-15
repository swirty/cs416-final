# @login_required(login_url='login')
# def home_page(request):
#     context = {'posts': Post.objects.filter(user=request.user).order_by('posted_at').reverse()}
#     return render(request, 'cosmos/user-profile.html', context)
#
#
# def user_page(request, user_id):
#     context = {'posts': Post.objects.filter(user_id=user_id).order_by('posted_at').reverse()}
#    return render(request, 'cosmos/user-profile.html', context)
import json

from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .models import Post
from .forms import create_post_form
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import create_post_form
from accounts.forms import EditProfileForm, EditProfileAboutForm, EditProfileProPicForm, EditProfileBannerPicForm
from .models import Post, Reaction, Follow
from accounts.models import Profile


@login_required(login_url='login')
def home(request):
    # TODO
    return redirect('user/' + str(request.user.id))


def user_profile(request, profile_user_id=None):
    if request.method == 'POST' and profile_user_id != None and profile_user_id == request.user.id:
        form = EditProfileForm(request.POST, instance=Profile.objects.get(user_id=profile_user_id))
        print('test')
        if form.is_valid():
            form.save()
            #print(str(form.data))
            #Profile(user_id=profile_user_id, )
    else:
        if profile_user_id is None:
            return redirect('landing')
        get_object_or_404(User, id=profile_user_id)
    context = {'posts': list(Post.objects.filter(user=profile_user_id).order_by('posted_at').reverse())[:15],
               'current_user': request.user,
               'profile_user': User.objects.get(id=profile_user_id).profile.user,
               'user_has_posts': Post.objects.filter(user=profile_user_id).count() != 0,
               'edit_user_profile_about_form': EditProfileAboutForm(),
               'edit_user_profile_pro_pic_form': EditProfileProPicForm(),
               'edit_user_profile_banner_pic_form': EditProfileBannerPicForm(),
               'form': EditProfileForm()}
    return render(request, 'cosmos/user-profile.html', context)



@login_required(login_url='login')
def edit_user_profile(request, profile_user_id, profile_field):
    print('edit profile request made')
    if request.method == 'POST' and profile_user_id == request.user.id:
        form = None
        print(profile_user_id)
        if profile_field == 'about':
            form = EditProfileAboutForm(request.POST, instance=Profile.objects.get(user_id=profile_user_id))
            print('\tabout')
        elif profile_field == 'pro_pic':
            form = EditProfileProPicForm(request.POST, request.FILES, instance=Profile.objects.get(user_id=profile_user_id))
            print('\tpro_pic')
        elif profile_field == 'banner_pic':
            form = EditProfileBannerPicForm(request.POST, request.FILES, instance=Profile.objects.get(user_id=profile_user_id))
            print('\tbanner_pic')
        if form.is_valid():
            form.save()
            print('\t\tSAVED')
        else:
            print(str(form.data))
    return redirect('/user/' + str(profile_user_id))



@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = create_post_form(request.POST)
        if form.is_valid():
            user = request.user
            post_body = form.cleaned_data['post_body']
            post = Post(user=user, post_body=post_body)
            post.save()
            return redirect('/')
    context = {'form': create_post_form(),
               'header_flavor': 'Create a Post',
               'button_flavor': 'Go!'}
    return render(request, 'cosmos/create-post.html', context)


@login_required(login_url='login')
def show_post(request, view_post=None):
    if request.method == 'POST' or view_post is None:
        return redirect('/')
    get_object_or_404(Post, id=view_post)

    context = {'posts': Post.objects.filter(id=view_post).union(Post.objects.filter(reply_id=view_post)),
               'current_user': request.user}
    return render(request, 'cosmos/post-thread.html', context)


@login_required(login_url='login')
def create_reply(request, other_post=None):
    if other_post is None:
        return redirect('landing')
    if request.method == 'POST':
        form = create_post_form(request.POST)
        if form.is_valid():
            user = request.user
            post_body = form.cleaned_data['post_body']
            post = Post(reply_id=other_post, user=user, post_body=post_body)
            post.save()
            return redirect('/')
    context = {'form': create_post_form(),
               'header_flavor': 'Create a Post',
               'button_flavor': 'Go!'}
    return render(request, 'cosmos/create-post.html', context)

# Render the next n posts after the specified ID and return them
# The posts come from the request user's follows if a specific user isn't identified.
@login_required(login_url='login')
def next_n_posts(request):
    if request.method == 'POST':

        # Filter posts from either the specified user or from the request user's follows by ID descending, excluding posts before the specified ID
        post_filter = Post.objects.filter()
        if request.POST['userID']:
            post_filter = post_filter.filter(user_id=request.POST['userID'])
        else:
            # follow_ids is a tuple of ids from all the users that request.user follows
            follow_ids = tuple([follow.to_user for follow in Follow.objects.filter(from_user_id=request.user.id)])
            post_filter = post_filter.filter(user_id__in=follow_ids)
        post_filter = post_filter.exclude(id__gte=request.POST['postID']).order_by('posted_at').reverse()

        # If a profile user id was supplied, grab its respective user for the context
        profile_user = None
        if request.POST['userID'] != '':
            profile_user = User.objects.get(id=int(request.POST['userID']))

        context = {
            'posts': post_filter[:int(request.POST['numberOfPosts'])],
            'current_user': request.user,
            'profile_user': profile_user,
            'user_has_posts': Post.objects.filter(user_id=request.POST['userID']).count() != 0,
        }
        return render(request, 'cosmos/post-render-container.html', context)

# the worst function in the entire project
@login_required(login_url='login')
def reaction_AJAX_operations(request):
    def like_return(postID):
        return HttpResponse(Reaction.objects.filter(reaction='LIKE', post_id=postID).count())

    def dislike_return(postID):
        return HttpResponse(Reaction.objects.filter(reaction='DISLIKE', post_id=postID).count())

    if request.method == 'GET':
        return redirect('landing')

    # setter db operations
    if request.POST['operation'] == 'SET':
        # get the reaction associated with this post and user
        react = Reaction.objects.filter(reaction=request.POST['goal'], post_id=request.POST['postID'],
                                        user_id=request.POST['userID'])
        # is there a reaction of type 'target' between this user and this post?
        if react.count() == 0:
            # no, create one, old QueryList in react can be clobbered
            react = Reaction(reaction=request.POST['goal'], post_id=request.POST['postID'],
                             user_id=request.POST['userID'])
            react.save()
        else:
            # yes, delete it
            react[0].delete()

    # getter db operations
    if request.POST['goal'] == 'LIKE':
        return like_return(request.POST['postID'])

    if request.POST['goal'] == 'DISLIKE':
        return dislike_return(request.POST['postID'])
