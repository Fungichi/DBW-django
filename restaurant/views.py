from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import review
from django.template import loader
from django.utils import timezone


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def ecologie(request):
    return render(request, 'ecologie.html')

def kindermenu(request):
    return render(request, 'kindermenu.html')


def locatie(request):
    return render(request, 'locatie.html')


def menu(request):
    return render(request, 'menu.html')

def openingsuren(request):
    return render(request, 'openingsuren.html')

def reservatie(request):
    template = loader.get_template("reservatie.html")
    return HttpResponse(template.render)
def volwassenmenu(request):
    return render(request, 'volwassenmenu.html')

