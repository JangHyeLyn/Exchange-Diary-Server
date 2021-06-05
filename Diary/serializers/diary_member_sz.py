from rest_framework.serializers import ModelSerializer
from ..models import Diary
from ..models import DiaryMember


class DiaryMemberSZ(ModelSerializer):
    class Meta:
        model = DiaryMember
        fields = ('id', 'nickname', 'diary',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        new_member = DiaryMember.objects.create(**validated_data)
        return new_member