from django.contrib import admin
from .models import Cars

# Register your models here.
@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('__str__',)