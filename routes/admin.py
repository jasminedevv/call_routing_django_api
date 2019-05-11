from django.contrib import admin
from .models import CarrierList, Price

# Register your models here.
admin.site.register(CarrierList)

admin.site.register(Price)