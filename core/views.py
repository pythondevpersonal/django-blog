from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, View

from core.models import Core

# Create your views here.

class IndexView(ListView):
    model: Core
    
    def get_queryset(self):
        return Core.objects.all()

class SingleView(View):
    model: Core
    
    def get_queryset(self):
        return Core.objects.all()