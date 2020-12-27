from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from ..models import Diary


class UserDiarySetSZ(HyperlinkedModelSerializer):
    class Meta:
        model = Diary
        fields = ['url', 'id', 'title']
