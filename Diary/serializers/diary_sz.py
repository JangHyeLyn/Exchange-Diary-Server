from django.db import transaction
from django.db.models import F
from django.core.exceptions import ValidationError

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

    def validate(self, attr):
        user = self.context.get('request').user
        group = attr.get('group')
        if not group:
            return attr
        try:
            DiaryGroup.objects.get(pk=group.id, user=user)
        except DiaryGroup.DoesNotExist as e:
            raise serializers.ValidationError({'group': e})
        return attr

    @transaction.atomic
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        validated_data['user'] = user
        validated_data['now_writer'] = user
        diary = Diary.objects.create(**validated_data)

        # diary_member create
        DiaryMember.objects.get_or_create(
            nickname=user.username,
            diary_id=diary.pk,
            user=user,
            profile_img=user.profile_img if user.profile_img else None,
        )
        return diary


class DiaryDetailSZ(ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'title', 'now_page', 'now_writer', 'total_page', 'cover', 'group',
                  'created_at',
                  'updated_at', ]

        read_only_fields = (
            "id", "now_page", 'now_writer_name', "total_page", 'group', "created_at", "updated_at")


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
