from django.shortcuts import render
from core.models import Part
from django.views.generic import  TemplateView , ListView 
from accounts.models import User
from django.urls import reverse_lazy

# Create your views here.

class MainView(TemplateView):
    template_name = "main-index.html"


class WinView(ListView):
    model = Part
    template_name = 'main2-index.html'
    context_object_name = 'parts'

class ShopListView(ListView):
    model = Part
    template_name = 'autopart-magazine-list.html'
    context_object_name = 'parts'

class ContactView(ListView):
    model = Part
    template_name = 'contact.html'
    context_object_name = 'parts'



class AboutView(ListView):
    model = Part
    template_name = 'aboutus.html'
    context_object_name = 'parts'