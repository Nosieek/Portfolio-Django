from django.shortcuts import render
from .models import Project
from django.views.generic import ListView, DetailView

# def project_index(request):
#     projects = Project.objects.all()
#     context = {
#         'projects': projects
#     }
#     return render(request, 'project_home.html', context)

class project_index(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'project_home.html'

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

# class project_detail(DetailView):
#     model = Project
#     pk_url_kwarg = 'pk'
#     context_object_name = 'projects'
#     template_name = 'project_detail.html'

