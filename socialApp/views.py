from django.shortcuts import render
from .models import Books
from django.views.generic import ListView
# Create your views here.

class Booklist(ListView):
    model = Books
    template_name = 'home.html'

