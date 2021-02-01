from rest_framework.serializers import ModelSerializer
from ..models import DiaryGroup

class DiaryGroupListSZ(ModelSerializer):
    class Meta:
        model = DiaryGroup
        fields = ['id', 'title', 'user', 'group_member_set', 'created_at', 'updated_at']
