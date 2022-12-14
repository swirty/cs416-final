from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='landing'),
    path('post/create', views.create_post, name='create_post'),
    path('post/reply/<int:other_post>/', views.create_reply, name='create_reply'),
    path('post/<int:view_post>/', views.show_post, name='query_post'),
    path('post/ajax', views.reaction_AJAX_operations, name='ajaxPost'),
    path('user/<int:profile_user>/', views.user_profile, name='queryUser'),
    path('user/', views.user_profile, name='queryUser'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    print("THIS PROJECT IS BEING DEBUGGED")