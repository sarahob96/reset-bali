from django.contrib import admin
from .models import Rewind, Renew, Restart

# Register your models here.

admin.site.register(Rewind)
admin.site.register(Restart)
admin.site.register(Renew)
