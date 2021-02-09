from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from Accounts.serializers import UserDiarySZ
from .diary_member_sz import DiaryMemberSZ
from ..models import Diary


class DiaryListSZ(ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'title', 'now_page', 'total_page', 'created_at', 'updated_at']


class DiaryDetailSZ(ModelSerializer):
    now_writer = UserDiarySZ(many=True, read_only=True)
    member = DiaryMemberSZ(source='member_set', many=True, read_only=True)

    class Meta:
        model = Diary
        fields = fields = ['id', 'title', 'now_page', 'now_writer', 'total_page', 'member', 'created_at',
                           'updated_at']
