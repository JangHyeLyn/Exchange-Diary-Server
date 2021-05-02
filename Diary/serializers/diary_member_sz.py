from rest_framework.serializers import ModelSerializer
from ..models import Diary
from ..models import DiaryMember


class DiaryMemberSZ(ModelSerializer):
    class Meta:
        model = DiaryMember
        fields = ['id', 'nickname', 'diary', 'created_at', 'updated_at']
        read_only_fields = ('id','created_at','updated_at')

    def create(self, validated_data):
        new_member = DiaryMember.objects.create(**validated_data, user=self.context.user)
        print(validated_data)
        return new_member