from django.contrib import admin
from .models import Post, Follow, Reaction, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Reaction)
admin.site.register(Profile)