from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView

from core.models import Core

# Create your views here.

class IndexView(ListView):
    model: Core
    context_object_name: 'latest_posts'
    
    def get_queryset(self):
        return Core.objects.all()