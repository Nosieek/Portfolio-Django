from django import forms
from .models import Post,Category

choises = Category.objects.all().values_list('name','name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'categories','author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put your title of post!'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Put your body of post!'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put your title of post!'}),
            #'categories': forms.Select(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Put your body of post!'}),
        }