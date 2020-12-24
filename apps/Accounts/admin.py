from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'profile_img', 'kakao_img', 'description', 'created_at', 'updated_at', ]