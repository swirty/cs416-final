from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import LoginForm

@login_required(login_url='login')
def home_page(request):
    context = {'posts': Post.objects.filter(user=request.user).order_by('posted_at').reverse()}
    return render(request, 'cosmos/user-profile.html', context)


def user_page(request, user_id):
    context = {'posts': Post.objects.filter(user_id=user_id).order_by('posted_at').reverse()}
    return render(request, 'cosmos/user-profile.html', context)