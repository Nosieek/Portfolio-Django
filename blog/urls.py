from django.urls import path
from . import views
from .views import BlogView, BlogDetailView, AddPostView,UpdatePostView,DeletePostView, AddCategoryView

urlpatterns = [
    path('', BlogView.as_view(), name="blog-home"),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('<int:pk>/delete_post/', DeletePostView.as_view(), name='delete-post'),
    path('edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path("<int:pk>/", BlogDetailView.as_view(), name='blog-detail'),
    path('<category>/', views.blog_category, name='blog-category'),

]