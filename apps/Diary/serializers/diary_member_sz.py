from rest_framework.serializers import ModelSerializer
from ..models import Diary, DiaryMember


class DiaryMemberSZ(ModelSerializer):
    class Meta:
        model = DiaryMember
        fields = ['id', 'nickname', 'diary', 'created_at', 'updated_at']


    def create(self, validated_data):
        new_member = DiaryMember.objects.create(**validated_data, user=self.context.user)
        return new_member