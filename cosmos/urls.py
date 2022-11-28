from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name="landing"),
    path('user/<int:user_id>', views.user_page, name="user_page")
    #path('register', views.register, name="register"),
    #path('login', views.login, name="login"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    print("THIS PROJECT IS BEING DEBUGGED")