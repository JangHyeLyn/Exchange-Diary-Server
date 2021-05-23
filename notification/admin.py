from django.contrib import admin
from notification.models import Notification


@admin.register(Notification)
class DiaryGroupAdmin(admin.ModelAdmin):
    list_display = ("id", "message", "created_at", "updated_at")