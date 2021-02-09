from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import Diary, DiaryMember
from rest_framework.response import Response
from ..serializers.diary_member_sz import DiaryMemberSZ
from django.db import transaction
from rest_framework import status


class DiaryMemberViewSet(ModelViewSet):
    queryset = DiaryMember.objects.all()
    serializer_class = DiaryMemberSZ
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print("Diary Member View Set create 진입")

        with transaction.atomic():
            diary = Diary.objects.get(pk=request.data['diary_id'])
            member = DiaryMember(
                nickname=request.data['nickname'],
                diary=diary
            )

            member.save()

            diary.member_set.add(member)
            request.user.mydiary_set.add(member)
            request.user.diary_set.add(diary)

            serializer = self.get_serializer(member)
            return Response(data=serializer.data)

        return Response(data=status.HTTP_400_BAD_REQUEST)
