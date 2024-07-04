from django.shortcuts import render
from django.http import HttpResponse
from .models import review
from django.template import loader
from django.utils import timezone
from django.shortcuts import render, redirect
from .forms import ReservatieForm
from .forms import ReviewForm
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
    if request.method == 'POST':
        form = ReservatieForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.pub_date = timezone.now()  # Assuming you want to set the current date and time
            review.save()
            return redirect('index.html')  # index.html
    else:
        form = ReservatieForm()

        return render(request, 'reservatie.html', {'form': form})

def volwassenmenu(request):
    return render(request, 'volwassenmenu.html')

def reviews_index(request):
    reviews = review.objects.all()
    context = {'reviews': reviews}
    template = loader.get_template("reviews.html")
    return HttpResponse(template.render(context,request))

def reviews_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.pub_date = timezone.now()  # Assuming you want to set the current date and time
            review.save()
            return redirect('index.html')  # index.html
    else:
        form = ReviewForm()

    return render(request, 'create_reviews.html', {'form': form})