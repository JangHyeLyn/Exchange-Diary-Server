from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from ..models import Diary


class NowWriterSZ(ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'title']
