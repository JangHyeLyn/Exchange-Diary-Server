from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from Accounts.serializers.user_diary_sz import UserDiarySZ
from .diary_member_sz import DiaryMemberSZ
from rest_framework import serializers
from ..models import Diary
from ..models import DiaryGroup
from ..models import DiaryGroupMember

class DiarySZ(ModelSerializer):
    group = serializers.SerializerMethodField()

    class Meta:
        model = Diary
        fields = ['id', 'title', 'now_page', 'total_page', 'user', 'now_writer', 'group', 'created_at', 'updated_at']
        read_only_fields = ("id", "now_page", "user", "now_writer", "created_at", "updated_at")

    def create(self, validated_data):
        user = self.context.get("request").user
        diary = Diary.objects.create(**validated_data, user=user, now_writer=user)
        return diary

    def get_group(self, obj, ):
        if obj.group:
            if DiaryGroup.objects.filter(pk=obj.group) is not None:
                DiaryGroupMember.objects.create(group=obj.group, diary=obj)
            return obj.group
        return 0


class DiaryDetailSZ(ModelSerializer):
    # members = DiaryMemberSZ(many=True, read_only=True)

    class Meta:
        model = Diary
        fields = ['id', 'title', 'now_page', 'now_writer', 'total_page', 'created_at',
                  'updated_at',]

        read_only_fields = ("id", "now_page", "total_page", "created_at", "updated_at")