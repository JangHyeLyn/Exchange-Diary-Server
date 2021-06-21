from django.db import transaction
from django.core.exceptions import ValidationError

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField

from ..models import Diary
from ..models import DiaryMember
from ..models import DiaryGroup

class DiaryMemberWithdrawlSZ(ModelSerializer):
    class Meta:
        model = DiaryMember
        fields = ['id', ]

