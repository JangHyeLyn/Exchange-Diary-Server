from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from Accounts.serializers.user_diary_sz import UserDiarySZ
from .diary_member_sz import DiaryMemberSZ
from ..models import Diary


class DiarySZ(ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'title', 'now_page', 'total_page', 'master', 'now_writer', 'created_at', 'updated_at']
        read_only_fields = ("id", "now_page", "master", "now_writer", "created_at", "updated_at")

    def create(self, validated_data):
        user = self.context.get("request").user
        diary = Diary.objects.create(**validated_data, master=user, now_writer=user)
        return diary


class DiaryDetailSZ(ModelSerializer):
    members = DiaryMemberSZ(many=True, read_only=True)

    class Meta:
        model = Diary
        fields = ['id', 'title', 'now_page', 'now_writer', 'total_page', 'created_at',
                  'updated_at', 'members', ]

        read_only_fields = ("id", "now_page", "total_page", "created_at", "updated_at")