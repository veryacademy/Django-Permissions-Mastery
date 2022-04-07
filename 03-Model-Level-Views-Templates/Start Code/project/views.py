from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import ProjectForm
from .models import Project


def index(request):
    return render(request, "index.html")

def project_listing(request):
    project_data = Project.objects.all()
    return render(request, "project.html", {"projects": project_data})

def project_detail(request, id):
    project = get_object_or_404(Project, slug=id)
    return render(request, "detail.html", {"detail": project})

def create_project(request):

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return HttpResponseRedirect(reverse("project:project"))
    else:
        form = ProjectForm()

    return render(request, "create_project.html", {"form": form})
