from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.

projectslist = [

    {
        "id": "1",
        "title": "E-commerce Website",
        "description": "Fully functional website"
    },
    {
        "id": "2",
        "title": "Portfolio website",
        "description": "This is a project where i built out my protfulio"
    },
    {
        "id": "3",
        "title": "Social Network",
        "description": "Awesome open-source project"
    },
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html',context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project':projectObj} )

 