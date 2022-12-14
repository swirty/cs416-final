from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='landing'),
    path('post/create', views.create_post, name='create_post'),
    path('post/reply/<int:other_post>/', views.create_reply, name='create_reply'),
    path('post/<int:view_post>/', views.show_post, name='query_post'),
    path('post/loadmore', views.next_n_posts, name='load_more_posts'),
    path('post/ajax', views.reaction_AJAX_operations, name='ajaxPost'),
    path('user/<int:profile_user_id>/', views.user_profile, name='query_user'),
    path('user/edit/<int:profile_user_id>/<str:profile_field>/', views.edit_user_profile, name='edit_user_profile'),
    path('user/', views.user_profile, name='query_user'),
    path('post/react', views.reaction_AJAX_operations, name='ajaxPost'),
    path('post/delete', views.delete_post, name='delete_post'),
    path('user/follow', views.follow_user, name='follow_user')
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    print("THIS PROJECT IS BEING DEBUGGED")