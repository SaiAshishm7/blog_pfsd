from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .models import BlogPost, Genre
from .forms import BlogPostForm


from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})

def blog_list(request):
    genre_filter = request.GET.get('genre')
    if genre_filter:
        posts = BlogPost.objects.filter(genre__name=genre_filter).order_by('-created_at')
    else:
        posts = BlogPost.objects.all().order_by('-created_at')
    genres = Genre.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts, 'genres': genres})

def post_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})