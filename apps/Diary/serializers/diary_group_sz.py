from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from rest_framework.serializers import DictField

from drf_writable_nested.serializers import WritableNestedModelSerializer

from .diary_group_member_sz import DiaryGroupMemberSZ
from ..models import DiaryGroup
from ..models import DiaryGroupMember


class DiaryGroupListSZ(ModelSerializer):
    count = SerializerMethodField()
    class Meta:
        model = DiaryGroup
        fields = ('id', 'title', 'rank', 'count', 'created_at', 'updated_at',)

    def get_count(self, obj):
        return obj.group_count(obj.pk)


class DiaryGroupCreateSZ(ModelSerializer):

    class Meta:
        model = DiaryGroup
        fields = ('id', 'title', 'user', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'user')


    def create(self, validated_data):
        user = self.context.get("request").user
        diarygroup = DiaryGroup.objects.create(**validated_data, user=user)
        return diarygroup

class DiaryGroupRetriveSZ(WritableNestedModelSerializer):

    class Meta:
        model = DiaryGroup
        fields = ('id', 'title', 'user', 'rank', 'created_at', 'updated_at', )
        read_only_fields = ('id', 'title', 'user', )

class DiaryGroupUpdateDeleteSZ(ModelSerializer):

    class Meta:
        model = DiaryGroup
        fields = ('id', 'title')