from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import Diary, DiaryGroup, DiaryGroupMember
from rest_framework.response import Response
from ..serializers.diary_group_member_sz import DiaryGroupMemberListSZ
from django.db import transaction
from rest_framework import status

class DiaryGroupMemberViewSet(ModelViewSet):
    queryset = DiaryGroupMember.objects.all()
    serializer_class = DiaryGroupMemberListSZ
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        group = DiaryGroup.objects.get(pk=self.request.data['group'])
        return DiaryGroupMember.objects.filter(group=group)

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            diary_group = DiaryGroup.objects.get(pk=request.data['group'])
            diary_group.group_member_set.all().delete()

            for rank, diary_id in enumerate(request.data['diaries']):
                diary = Diary.objects.get(pk=diary_id)
                diary_group_member = DiaryGroupMember(
                    rank=rank + 1
                )
                diary_group_member.save()
                diary_group.group_member_set.add(diary_group_member)
                diary.group_diary_set.add(diary_group_member)

            serializer = self.get_serializer(diary_group_member)
            return Response(data=serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST)

