from django.shortcuts import render

def index(request):
    return render(request, 'resume/index.html')
from django.views.generic import TemplateView

