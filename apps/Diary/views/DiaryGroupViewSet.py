from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import DiaryGroup
from rest_framework.response import Response
from ..serializers.diary_group_sz import DiaryGroupListSZ
from django.db import transaction
from rest_framework import status

class DiaryGroupViewSet(ModelViewSet):
    queryset = DiaryGroup.objects.all()
    serializer_class = DiaryGroupListSZ
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DiaryGroup.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        print("Diary Group View Set create 진입")
        with transaction.atomic():
            diary_group = DiaryGroup(
                title=request.data['title'],
                user=request.user
            )

            diary_group.save()
            request.user.user_diary_group_set.add(diary_group)
            serializer = self.get_serializer(diary_group)

            return Response(data=serializer.data)
        return Response(data=status.HTTP_400_BAD_REQUEST)