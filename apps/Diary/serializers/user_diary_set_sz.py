from rest_framework.serializers import ModelSerializer
from ..models import Diary
class UserDiarySetSZ(ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id','title']