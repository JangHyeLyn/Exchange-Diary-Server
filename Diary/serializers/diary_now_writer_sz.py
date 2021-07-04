from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from ..models import Diary


class DiaryNowWriterSZ(ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'title', 'now_page', 'total_page', 'user', 'now_writer', 'cover', 'group', 'created_at',
                  'updated_at']
        read_only_fields = ("id", "now_page", "user", "now_writer", "created_at", "updated_at")
