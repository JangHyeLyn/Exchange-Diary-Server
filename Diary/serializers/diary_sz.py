from django.db import transaction
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from django.shortcuts import get_object_or_404
from Accounts.serializers.user_diary_sz import UserDiarySZ
from .diary_member_sz import DiaryMemberSZ
from rest_framework import serializers
from ..models import Diary
from ..models import DiaryMember
from ..models import DiaryGroup
from ..models import DiaryGroupMember

class DiarySZ(ModelSerializer):

    class Meta:
        model = Diary
        fields = ['id', 'title', 'now_page', 'total_page', 'user', 'now_writer', 'cover', 'created_at', 'updated_at']
        read_only_fields = ("id", "now_page", "user", "now_writer", "created_at", "updated_at")

    @transaction.atomic()
    def create(self, validated_data):
        request = self.context.get("request")
        diary = Diary.objects.create(**validated_data, user=request.user, now_writer=request.user)
        if 'group' in request.data:
            DiaryGroupMember.objects.create(group=DiaryGroup.objects.get(pk=request.data.get('group')), diary=diary)
        return diary


class DiaryDetailSZ(ModelSerializer):
    # members = DiaryMemberSZ(many=True, read_only=True)
    group = serializers.SerializerMethodField()
    class Meta:
        model = Diary
        fields = ['id', 'title', 'now_page', 'now_writer', 'total_page', 'cover', 'group', 'created_at',
                  'updated_at',]

        read_only_fields = ("id", "now_page", "total_page", "created_at", "updated_at")

    def get_group(self, obj):
        try:
            group_member = DiaryGroupMember.objects.get(diary=obj)
            return group_member.group_id
        except DiaryGroupMember.DoesNotExist:
            return 0

class DiaryMeSZ(ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'title', 'now_page', 'total_page', 'user', 'now_writer', 'cover', 'created_at', 'updated_at']
        read_only_fields = ("id", "now_page", "user", "now_writer", "created_at", "updated_at")
