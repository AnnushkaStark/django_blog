from django.contrib import admin
from .models import Post, Comment,Like

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'text_comment', 'date', 'post')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('ip',)