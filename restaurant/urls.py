from django.urls import path

from . import views

urlpatterns = [
    path("index.html", views.index, name="index"),
    path("", views.index, name="index"),
    path("ecologie.html",views.ecologie,name="ecologie"),
    path("kindermenu.html", views.kindermenu, name="kindermenu"),
    path("volwassenmenu.html", views.volwassenmenu, name="volwassenenmenu"),
    path("locatie.html", views.locatie, name="locatie"),
    path("menu.html", views.menu, name="menu"),
    path("openingsuren.html", views.openingsuren, name="openingsuren"),
    path("reservatie.html", views.reservatie, name="reservatie"),
    path("about.html", views.about, name="about"),
    

]