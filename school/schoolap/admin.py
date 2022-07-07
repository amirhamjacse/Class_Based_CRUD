from django.contrib import admin
from .models import Database1
# Register your models here.
@admin.register(Database1)
class DataAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'registration', 'department']