from django.shortcuts import render
from .models import Project
# Create your views here.

def portfolio(request):
    projects=Project.objects.all()
    return render(request,'portfolio/portfolio.html', {'projects': projects})

def project_detail(request, project_id):
    # Fetch a specific project based on project_id from the database
    project = Project.objects.get(pk=project_id)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def contact(request):
    # Define your contact view logic here
    return render(request, 'portfolio/contact.html')