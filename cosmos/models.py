import os

from django.db import models
from django.contrib.auth.models import User
from PIL import ImageOps

# Create your models here.


# Each user maps to one profile, many posts, many reactions, and many follows


# Each profile maps to one user


# Each post maps to one user and many reactions.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey('self', blank=True, null=True, on_delete=models.DO_NOTHING)
    post_body = models.CharField(max_length=250)
    posted_at = models.DateTimeField(auto_now_add=True) # auto_now captures the UPDATE time, as opposed to the CREATION time

    # This field allows for posts to contain images
    def post_image_directory(instance, filename):
        return 'uploads/posts/{0}/'.format(instance.user.id)
    post_images = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.user.username + ": " + self.post_body


# Each reaction maps to one user and one post
class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=1)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " " + self.reaction + "'s " + self.post.post_body


# Each follow maps to two users
class Follow(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user")

    def __str__(self):
        return self.from_user.username + " follows " + self.to_user.username