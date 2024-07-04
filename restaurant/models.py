from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class review(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    stars = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.text

class reservatie(models.Model):
    voornaam = models.CharField(max_length=50)
    achternaam = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    aantal_pers = models.IntegerField()
    res_date = models.DateTimeField("Reservation date")  # Use DateTimeField for date and time
    res_time = models.TimeField("Reservation time")

    def __str__(self):
        return f"{self.voornaam} {self.achternaam}"