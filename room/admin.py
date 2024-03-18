from django.contrib import admin
from .models import Rooms_type, Rooms, Capacity


# Register your models here
admin.site.register([Rooms_type, Rooms, Capacity])