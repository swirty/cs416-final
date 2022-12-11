from django.contrib import admin
from .models import Post, Follow, Reaction
from accounts.models import Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Reaction)