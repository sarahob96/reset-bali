from django.db import models

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=20)
    programme_attended = models.CharField(max_length=20)
    Your_experience = models.TextField(max_length = 400)