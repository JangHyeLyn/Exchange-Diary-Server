from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .diary_member_sz import DairyMemberSZ
from ..models import Diary


class DiaryListSZ(ModelSerializer):
    class Meta:
        model = Diary
        fields = [ 'id', 'title', 'now_page', 'total_page', 'created_at', 'updated_at', ]


class DiaryDetailSZ(ModelSerializer):
    member_set = DairyMemberSZ(many=True, read_only=True)

    class Meta:
        model = Diary
        fields = ['id', 'title', 'now_page', 'total_page', 'created_at', 'updated_at', 'member_set']
