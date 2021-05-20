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
        fields = ("id", "message", "created",)

    def get_diary_title(self):
        pass

    def get_diary_cover(self):
        pass

    def get_diary_status(self):
        pass

    def get_diary_group(self):
        pass
