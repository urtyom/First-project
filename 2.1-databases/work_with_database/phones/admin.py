from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Phone

# Register your models here.
@admin.register(Phone)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'price',
        'image',
        'release_date',
        'lte_exists',
        'slug'
        ]
    list_filter = ['name', 'price',]
