from rest_framework import serializers

class DiaryGroupIdSZ(serializers.Serializer):
    group = serializers.IntegerField(default=0)