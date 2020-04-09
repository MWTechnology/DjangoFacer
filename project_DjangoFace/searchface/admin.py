from django.contrib import admin
from .models import Mysearchface
# Register your models here.

@admin.register(Mysearchface)
class UserAdmin(admin.ModelAdmin):
    list_display = ['author', 'image']