from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return f'Title: {self.title}\n author: {self.author}'

    def get_absolute_url(self):
        return reverse('blog-home')


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Category: {self.name}"

    def get_absolute_url(self):
        return reverse('blog-home')