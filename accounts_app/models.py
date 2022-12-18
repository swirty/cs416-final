from django.db import models
from django.contrib.auth.models import User
from PIL import ImageOps
from django_resized import ResizedImageField

import os

# Create your models here.

# Each profile maps to one user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=250, default="Hello, Cosmos! I haven't written a bio yet...")

    def profile_pic_directory(instance, filename: str):
        print(os.getcwd())
        return '/uploads/profile/{0}/pfp'.format(instance.user.id)
    pro_pic = ResizedImageField(size=[256, 256], scale=None, crop=['middle', 'center'], keep_meta=False, force_format='PNG', null=True, default="default-pro-pic.png")

    def banner_pic_directory(instance, filename: str):
        return 'uploads/profile/{0}/banner'.format(instance.user.id)
    banner_pic = ResizedImageField(size=[1280, 320], scale=None, crop=['middle', 'center'], keep_meta=False, force_format='PNG', null=True, default="default-banner-pic.png")

    def __str__(self):
        return self.user.username + "\'s profile"