from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def homePage(request):
    context = {'posts': Post.objects.filter(user=request.user).order_by('posted_at').reverse()}
    return render(request, 'cosmos/user-profile.html', context)

def deliver_css(request):
    print(request.path)
    return render(content_type='css')
