# showroom/admin.py

from django.contrib import admin
from .models import Mobil, Service

admin.site.register(Mobil)
admin.site.register(Service)
