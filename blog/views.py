from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView,CreateView,UpdateView, DeleteView
from .forms import PostForm,EditForm
from django.urls import reverse_lazy

class BlogView(ListView):
    model = Post
    template_name = 'blog_home.html'
    ordering = ['-last_modified']

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context) #przerob

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title','categories','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog-home')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'



