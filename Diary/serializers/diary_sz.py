from django.db import transaction

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField

from ..models import Diary
from ..models import DiaryMember
from ..models import DiaryGroup


class DiarySZ(ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'title', 'now_page', 'total_page', 'user', 'now_writer', 'cover', 'group', 'created_at',
                  'updated_at']
        read_only_fields = ("id", "now_page", "user", "now_writer", "created_at", "updated_at")

    @transaction.atomic()
    def create(self, validated_data):
        request = self.context.get("request")
        try:
            DiaryGroup.objects.get(pk=self.data.get('group'), user=request.user)
        except DiaryGroup.DoesNotExist as e:
            raise serializers.ValidationError({'group': e})
        diary = Diary.objects.create(**validated_data, user=request.user, now_writer=request.user)
        return diary


class DiaryDetailSZ(ModelSerializer):
    # members = DiaryMemberSZ(many=True, read_only=True)

    class Meta:
        model = Diary
        fields = ['id', 'title', 'now_page', 'now_writer', 'total_page', 'cover', 'group', 'created_at',
                  'updated_at', ]

        read_only_fields = ("id", "now_page", "total_page", "created_at", "updated_at")


class DiaryMeSZ(ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'title', 'now_page', 'total_page', 'user', 'now_writer', 'cover', 'group', 'created_at',
                  'updated_at']
        read_only_fields = (
            'id', 'title', 'now_page', 'total_page', 'user', 'now_writer', 'cover', 'group', 'created_at', 'updated_at')


class DiaryInGroupSZ(ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'title', ]
        read_only_fields = ('id', 'title',)
