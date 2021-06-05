from ..models import Notification

from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField


class NotificationListSZ(ModelSerializer):
    diary_title = SerializerMethodField(default="")
    diary_cover = SerializerMethodField(default="")
    diary_status = SerializerMethodField(default="")
    diary_group = SerializerMethodField(default="")

    class Meta:
        model = Notification
        fields = ("id", "diary_title", "diary_cover", "diary_status", "diary_group", "message", "created_at", "updated_at")

    def get_diary_title(self, obj):
        return obj.diary.title
        return "diary_title"

    def get_diary_cover(self, obj):
        return obj.diary.cover

    def get_diary_status(self, obj):
        return "diary_status"

    def get_diary_group(self, obj):
        return obj.diary.group if obj.diary.group else 0
