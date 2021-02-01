from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from ..models import Diary
from ..models import DiaryGroup

class DiaryGroupAddSZ(ModelSerializer):

    class Meta:
        model = DiaryGroup
        fields = ['id', 'title', 'user','diary','created_at', 'updated_at']

    def create(self, validated_data):
        diary_group_data = {
            'title': validated_data.data['title'],
            'user': validated_data.user,
        }
        #print("asdfasdf")
        #print(validated_data.data['diary'])
        #print(Diary.objects.filter(id=validated_data.data['diary']))
        if 'diary' in validated_data.data:
            for diary in validated_data.data['diary']:
                diary_group_data.update({'diary': Diary.objects.filter(id=diary)})
        diary_group = super().create(diary_group_data)

        return diary_group
