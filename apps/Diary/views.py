from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Diary, DiaryGroup, DiaryMember
from rest_framework.response import Response
from .serializers.diary_list_sz import DiaryListSZ, DiaryDetailSZ
from .serializers.diary_group_sz import DiaryGroupListSZ
from .serializers.diary_member_sz import DiaryMemberSZ
from Accounts.models import User
from django.db import transaction
from rest_framework import status


class DiaryViewSet(ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiaryListSZ
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        serializer = DiaryDetailSZ(self.get_object())
        return Response(data=serializer.data)

    def create(self, request, *args, **kwargs):
        print('DiaryViewSet create 진입')

        with transaction.atomic():
            diary = Diary(
                title=request.data['title'],
            )
            if 'total_page' in request.data:
                diary.total_page = request.data['total_page']

            diary.save()

            request.user.diary_set.add(diary)
            request.user.now_writer_set.add(diary)

            serializer = self.get_serializer(diary)
            return Response(data=serializer.data)

        return Response(data=status.HTTP_400_BAD_REQUEST)


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

