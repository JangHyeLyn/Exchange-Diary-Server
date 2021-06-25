from ..models import Notification

from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField


class NotificationListSZ(ModelSerializer):
    diary_id = SerializerMethodField()
    diary_title = SerializerMethodField(default="")
    diary_cover = SerializerMethodField(default="")
    diary_status = SerializerMethodField(default="")
    diary_group = SerializerMethodField(default="")

    class Meta:
        model = Notification
        fields = ("id", "diary_id", "diary_title", "diary_cover", "diary_status", "diary_group", "message", "created_at")

    @staticmethod
    def get_diary_id(obj):
        return obj.diary.pk

    @staticmethod
    def get_diary_title(obj):
        return obj.diary.title

    @staticmethod
    def get_diary_cover(obj):
        return obj.diary.cover

    @staticmethod
    def get_diary_status(obj):
        return obj.diary.status

    @staticmethod
    def get_diary_group(obj):
        return obj.diary.group
