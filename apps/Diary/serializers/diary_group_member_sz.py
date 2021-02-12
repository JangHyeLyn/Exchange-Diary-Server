from rest_framework.serializers import ModelSerializer
from ..models import DiaryGroupMember


class DiaryGroupMemberSZ(ModelSerializer):
    class Meta:
        model = DiaryGroupMember
        fields = ['id', 'rank', 'group', 'diary', 'created_at', 'updated_at']
