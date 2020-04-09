from django.contrib import admin
from .models import Suspect
# Register your models here.

@admin.register(Suspect)
class UserAdmin(admin.ModelAdmin):
    list_display = ['author','surname', 'name', 'patronymic']
