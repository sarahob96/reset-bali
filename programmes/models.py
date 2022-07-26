from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
booking_status = (("pending", "pending"),
                  ("approved", "approved"),
                  ("booked-out", "booked-out"))

dates_rewind = (
        ("05/05/2023-08/05/2023", "05/05/2023-08/05/2023"),
        ("14/05/2023-17/05/2023", "14/05/2023-17/05/2023"),
        ("25/05/2023-28/06/2023", "25/05/2023-28/06/2023"),
        ("04/06/2023-07/06/2023", "04/06/2023-07/06/2023"),
        ("14/06/2023-17/06/2023", "14/06/2023-17/06/2023"),
        ("04/07/2023-07/07/2023", "04/07/2023-07/07/2023"),
        ("12/07/2023-15/07/2023", "12/07/2023-15/07/2023"),
        ("22/07/2023-25/07/2023", "22/07/2023-25/07/2023"),
        ("08/08/2023-11/07/2023", "08/08/2023-11/07/2023"),
)

dates_restart = (
        ("13/05/2023-18/05/2023", "13/05/2023-18/05/2023"),
        ("24/05/2023-29/05/2023", "24/05/2023-29/05/2023"),
        ("08/06/2023-13/06/2023", "08/06/2023-12/06/2023"),
        ("21/06/2023-26/06/2023", "21/06/2023-26/06/2023"),
        ("13/07/2023-18/07/2023", "13/07/2023-18/07/2023"),
        ("15/08/2023-20/08/2023", "15/08/2023-20/08/2023"),
)

dates_renew = (
        ("12/05/2023-19/05/2023", "12/05/2023-19/05/2023"),
        ("09/06/2023-16/06/2023", "09/06/2023-16/06/2023"),
        ("15/07/2023-22/07/2023", "15/07/2023-22/07/2023"),
        ("02/08/2023-09/08/2023", "02/08/2023-09/08/2023"),
        ("20/08/2023-27/08/2023", "20/08/2023-27/08/2023"),
        
)


class rewind(models.Model):
    """
    """
    PROGRAMMES = (("Rewind", "Rewind"), ("Renew", "Renew"), ("Restart", "Restart"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    programme = models.CharField(max_length=10, choices=PROGRAMMES, default="Rewind")
    date = models.CharField(max_length=25, choices=dates_rewind, default="05/05/2023-08/05/2023")
    status = models.CharField(max_length=10, choices=booking_status, default="pending")
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)

class booking(models.Model):
    booking_spaces = models.IntegerField()
    
