from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from ..models import DiaryMember
from .now_writer_set_sz import NowWriterSZ
from Accounts.serializers.user_diary_member_sz import UserDiaryMemberSZ

class DairyMemberSZ(ModelSerializer):
    user_set = UserDiaryMemberSZ(many=True, read_only=True)

    class Meta:
        model = DiaryMember
        fields = ['id', 'nickname', 'user', 'created_at', 'updated_at', 'user_set',]
