from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from ..models import Diary


class NowWriterSZ(HyperlinkedModelSerializer):
    class Meta:
        model = Diary
        fields = ['url', 'id', 'title']
