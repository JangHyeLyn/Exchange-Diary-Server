from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','profile','description','created_at','updated_at',]
    pass
