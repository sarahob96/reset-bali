from django.db import models

# Create your models here.

class login(models.Model):

    userName = models.CharField(max_length=20)
    userPassword = models.CharField(max_length=20)

class newUser(models.Model):

    userName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    userPassword = models.CharField(max_length=20)
    userPasswordRepeat = models.CharField(max_length=20)
    
