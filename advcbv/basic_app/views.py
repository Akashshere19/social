from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models   # . means current directory
#from django.http import HttpResponse
# Create your views here.
class IndexView(TemplateView):
    template_name ='index.html'

class SchoolListView(ListView):
    #school_list
    context_object_name = 'schools'
    model = models.School
    template_name = "basic_app/school_list.html"

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name ='basic_app/school_details.html'
class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School
    

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
