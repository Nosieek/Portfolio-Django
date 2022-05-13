from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# def blog_home(request):
#     return render(request, 'blog_home.html', {})

class BlogView(ListView):
    model = Post
    template_name = 'blog_home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
