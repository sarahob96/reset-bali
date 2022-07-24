from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class rewind(models.Model):
    """
    """
    PROGRAMMES = (("Rewind", "Rewind"), ("Renew", "Renew"), ("Restart", "Restart"))
    
    programme = models.CharField(max_length=20, choices=PROGRAMMES, default="Rewind")
    date = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()


def __str__(self):
    return self.username
