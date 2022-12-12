from django.urls import path, include
from . import views

urlpatterns = [
    path('account/edit', views.edit_user, name='edit_user'),
    path('account/signup', views.create_user, name='create_user'),
    path('account/', include('django.contrib.auth.urls'), name="login_page"),
]