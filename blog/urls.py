from django.urls import path
# from . import views
from .views import BlogView, BlogDetailView

urlpatterns = [
    path('', BlogView.as_view(), name="blog-home"),
    path("<int:pk>/", BlogDetailView.as_view(), name='blog-detail'),
]