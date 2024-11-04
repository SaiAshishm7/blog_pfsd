# blog/admin.py
from django.contrib import admin
from .models import BlogPost, Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'created_at')
    list_filter = ('genre', 'created_at', 'author')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    raw_id_fields = ('author',)