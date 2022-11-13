from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    context = {}
    return render(request, 'navbar-template.html', context)
