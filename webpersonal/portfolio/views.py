from django.shortcuts import render
from .models import Project


# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    recent_projects = Project.objects.order_by('-created')[:3]
    return render(request, "portfolio/portfolio.html", {'projects': projects, 'recent_projects': recent_projects})
