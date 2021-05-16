# from rest_framework.serializers import ModelSerializer, SerializerMethodField
# from ..models import DiaryGroupMember
#
#
# class DiaryGroupMemberSZ(ModelSerializer):
#     diary_title = SerializerMethodField()
#
#     class Meta:
#         model = DiaryGroupMember
#         fields = ['id', 'rank', 'diary', 'diary_title', 'created_at', 'updated_at']
#
#     def create(self, validated_data):
#         member = DiaryGroupMember.objects.create(**validated_data)
#         return member
#
#     def get_diary_title(self, obj):
#         return obj.diary.title