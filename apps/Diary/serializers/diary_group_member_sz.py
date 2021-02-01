from rest_framework.serializers import ModelSerializer
from ..models import Diary, DiaryGroup,DiaryMember
from .diary_list_sz import DiaryListSZ

class DiaryGroupMemberListSZ(ModelSerializer):
    class Meta:
        model = DiaryMember
        fields = ['id', 'rank', 'diary','created_at', 'updated_at']