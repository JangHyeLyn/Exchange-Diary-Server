from rest_framework.serializers import ModelSerializer
from ..models import Diary, DiaryMember


class DiaryMemberSZ(ModelSerializer):
    class Meta:
        model = DiaryMember
        fields = ['id', 'nickname', 'diary', 'created_at', 'updated_at']


