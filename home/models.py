from django.db import models


# Create your models here.


class Review(models.Model):
    """
    Review model for users to leave a review
    """

    STARS = ((1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five"))
    PROGRAMMES = (("Rewind", "Rewind"), ("Renew", "Renew"),
                  ("Restart", "Restart"))

    name = models.CharField(max_length=20)
    programme_attended = models.CharField(max_length=20, choices=PROGRAMMES)
    your_experience = models.TextField(max_length=400)
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(choices=STARS)


def __str__(self):
    return self.title
