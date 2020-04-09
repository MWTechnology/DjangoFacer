from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email', 'number', 'is_active']
    list_editable = ('is_active',)
    prepopulated_fields = {'email': ('number',)}

