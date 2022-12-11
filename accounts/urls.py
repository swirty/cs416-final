from django.urls import path, include
from . import views

urlpatterns = [
    path('account/edit', views.editUser, name='editUser'),
    path('account/signup', views.createUser, name='createUser'),
    path('account/', include('django.contrib.auth.urls'), name="loginPage"),
]