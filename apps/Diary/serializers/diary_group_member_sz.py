from rest_framework.serializers import ModelSerializer
from ..models import DiaryGroupMember


class DiaryGroupMemberListSZ(ModelSerializer):
    class Meta:
        model = DiaryGroupMember
        fields = ['id', 'rank', 'group', 'diary', 'created_at', 'updated_at']
