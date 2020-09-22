from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy
# simple Example of class based view for printing some line

#class CBView(View):
#    def get(self,request):
#        return HttpResponse("Class based views are pretty cool")


# Create your views here.
class IndexView(TemplateView):
    template_name='advanced_app/index.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['injectme']="Class based template view and basic injection"
        return context

class SchoolListView(ListView):
    model=models.School
#ListView by default returns context object name as school_list ie lowercase model name and add _list

class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    model=models.School
    template_name='advanced_app/school_detail.html'
#Detail view by default returns context name as lowercase of model name ie school
#if we wish to use different name then we edit attribute called context_object_name

class SchoolCreateView(CreateView):
    fields=('name','principal','location')
    model=models.School

class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model=models.School

class SchoolDeleteView(DeleteView):
    model=models.School
    success_url=reverse_lazy("advanced_app:list")
