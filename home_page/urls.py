from django.urls import path, include
from . import views
from .views import project_index

urlpatterns = [
    path("", project_index.as_view(), name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]