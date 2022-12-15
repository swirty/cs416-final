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
from .models import Post, Reaction, Follow


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
               'form': EditProfileForm(),
               'post_form': create_post_form()}
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
    return HttpResponse(create_post_form())


@login_required(login_url='login')
def show_post(request, view_post=None):
    if request.method == 'POST' or view_post is None:
        return redirect('/')
    get_object_or_404(Post, id=view_post)

    context = {'posts': Post.objects.filter(id=view_post).union(Post.objects.filter(reply_id=view_post)),
               'current_user': request.user}
    return render(request, 'cosmos/post-thread.html', context)


@login_required(login_url='login')
def create_reply(request, other_post):
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
               'button_flavor': 'Go!',
               'other_post': other_post}
    return render(request, 'cosmos/create-reply.html', context)

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

@login_required(login_url='login')
def delete_post(request):
    if request.method == 'GET':
        return redirect('landing')

    post_object = Post.objects.get(id=request.POST['postID'])

    # Does the post exist?
    if post_object is None:
        return HttpResponse(1)

    # print('post exists')

    # Does the request user own the post?
    if post_object.user_id != int(request.POST['userID']):
        return HttpResponse(1)

    # print('user owns post')

    # Delete the post and return success
    post_object.delete()
    # print('post deleted')

    return HttpResponse(0)

@login_required(login_url='login')
def follow_user(request):
    if request.method == 'GET':
        return redirect('landing')

    follow_object = Follow.objects.filter(from_user_id=request.POST['fromUserID'], to_user_id=request.POST['toUserID'])

    if request.POST['operation'] == 'GET':
        if follow_object.count() == 0:
            return HttpResponse("Follow")
        else:
            return HttpResponse("Unfollow")
    else:
        if follow_object.count() == 0:
            new_follow = Follow(from_user_id=request.POST['fromUserID'], to_user_id=request.POST['toUserID'])
            new_follow.save()
            return HttpResponse("Unfollow")
        else:
            follow_object[0].delete()
            return HttpResponse("Follow")