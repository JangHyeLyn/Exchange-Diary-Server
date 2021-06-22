from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from ..models import Diary
from ..models import DiaryMember


class DiaryMemberSZ(ModelSerializer):
    profile_img = SerializerMethodField()

    class Meta:
        model = DiaryMember
        fields = ('id', 'diary', 'nickname', 'profile_img', 'user_id')
        read_only_fields = ('id', 'diary', 'user_id')

    def get_profile_img(self, obj):
        if obj.profile_img:
            return obj.profile_img.url
        return self.context.get('request').user.profile_img.url

    def validate(self, attr):
        user = self.context.get('request').user
        diary_id = self.context.get('request').parser_context.get('kwargs').get('diary_pk')
        if DiaryMember.objects.filter(user=user, diary_id=diary_id):
            raise serializers.ValidationError({"error": "이미 가입 되어 있습니다"})
        try:
            attr['nickname'] = user.username
            attr['user'] = user
            attr['diary'] = Diary.objects.get(pk=diary_id)
        except Diary.DoesNotExist as e:
            raise serializers.ValidationError({'error': e})
        return attr

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['nickname'] = user.username
        new_member = DiaryMember.objects.create(**validated_data)
        return new_member


class DiaryMemberMeSZ(ModelSerializer):
    profile_img = SerializerMethodField()

    class Meta:
        model = DiaryMember
        fields = ('id', 'diary', 'nickname', 'profile_img', 'user_id')
        read_only_fields = ('id', 'diary', 'user_id')

    def get_profile_img(self, obj):
        if obj.profile_img:
            return obj.profile_img.url
        profile_img = self.context.get('request').user.profile_img
        return profile_img.url if profile_img else None

    def validate(self, attrs):
        profile_img = self.context.get('request').FILES.get('profile_img')
        try:
            self.instance.profile_img = profile_img
        except Exception as e:
            return attrs
        attrs['profile_img'] = profile_img
        return attrs