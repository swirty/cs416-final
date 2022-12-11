from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homePage, name='landing'),
    path('post/create', views.createPost, name='createPost'),
    path('post/reply/<int:other_post>', views.createReply, name='createReply'),
    path('post/<int:view_post>', views.showPost, name='queryPost'),
    path('post/ajax', views.ajaxOperations, name='ajaxPost'),
    path('user/<int:other_user>', views.showProfile, name='queryUser'),
    path('user/', views.showProfile, name='queryUser'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    print("THIS PROJECT IS BEING DEBUGGED")