from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from app.models import *

class SchooList(ListView):
    model=School
    context_object_name='schools'
    #queryset=School.objects.all()
    #template_name='school_list.html'