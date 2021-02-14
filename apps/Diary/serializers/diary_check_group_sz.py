from rest_framework.serializers import ModelSerializer
from ..models import DiaryGroup


class DiaryGroupSZ(ModelSerializer):
    class Meta:
        model = DiaryGroup
        fields = ('id', 'title', 'rank', 'user', 'created_at', 'updated_at',)
        read_only_fields = ("user", "group_member_set",)

    def create(self, validated_data):
        user = self.context.get('request').user
        group = DiaryGroup.objects.create(**validated_data, user=user)
        return group
