from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from ..models import Diary


class UserDiarySetSZ(ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'title']
