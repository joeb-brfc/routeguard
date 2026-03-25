from django.contrib import admin
from .models import Driver, Route, Availability, Assignment

admin.site.register(Driver)
admin.site.register(Route)
admin.site.register(Availability)
admin.site.register(Assignment)