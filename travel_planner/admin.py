from django.contrib import admin
from .models import Voyage,Reservation,Hebergement

admin.site.register(Voyage)
admin.site.register(Hebergement)
admin.site.register(Reservation)