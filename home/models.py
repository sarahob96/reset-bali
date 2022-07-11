from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STARS = ((1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five"))


class Review(models.Model):
    title = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    programme_attended = models.CharField(max_length=50)
    Your_experience = models.TextField(max_length=400)
    Date = models.DateTimeField(auto_now_add=True)
    Rating = models.IntegerField(choices=STARS, default=0)

def __str__(self):
    return self.title

