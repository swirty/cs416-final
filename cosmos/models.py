from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Each user maps to many posts, many reactions, and many follows


# Each post maps to one user and many reactions.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_body = models.CharField(max_length=250)
    posted_at = models.DateTimeField(auto_now_add=True) # auto_now captures the UPDATE time, as opposed to the CREATION time
    # post_image = models.ImageField()

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