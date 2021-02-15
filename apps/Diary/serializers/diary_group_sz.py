from drf_yasg.utils import swagger_serializer_method
from rest_framework.serializers import ModelSerializer, SerializerMethodField, BooleanField
from ..models import DiaryGroup, DiaryGroupMember


class DiaryGroupSZ(ModelSerializer):
    is_group = SerializerMethodField()

    class Meta:
        model = DiaryGroup
        fields = ('id', 'title', 'rank', 'user', 'members', 'is_group', 'created_at', 'updated_at',)
        read_only_fields = ('id', "user", "group_member_set",)

    def create(self, validated_data):
        user = self.context.get('request').user
        group = DiaryGroup.objects.create(**validated_data, user=user)
        return group

    @swagger_serializer_method(serializer_or_field=BooleanField)
    def get_is_group(self, obj):
        is_member = obj.members.all().filter(diary=self.context.get('diary_pk'))
        if is_member:
            return True
        else:
            return False
