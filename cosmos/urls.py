from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homePage, name="landing"),
    path('account/edit', views.editUser, name='editUser'),
    path('account/', include('django.contrib.auth.urls'), name="loginPage"),
    #path('/css', views.deliver_css, name="css"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

