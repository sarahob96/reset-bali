from django.db import models

# Create your models here.


class rewind(models.Model):
    """
    """

    STARS = ((1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five"))

    name = models.CharField(max_length=20)
    programme_attended = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()