from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from ..models import Diary


class DiaryListSZ(HyperlinkedModelSerializer):
    class Meta:
        model = Diary
        fields = ['url', 'id', 'title', 'now_page', 'total_page', 'created_at', 'updated_at']
