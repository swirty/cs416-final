from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homePage, name="landing"),
    #path('/css', views.deliver_css, name="css"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

