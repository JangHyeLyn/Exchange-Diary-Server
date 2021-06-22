from django.db import transaction
from django.views import View
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status, viewsets, mixins

from config.pagination import LargeResultsSetPagination
from Diary.tasks import add
from Diary.models import Diary
from Diary.models import DiaryMember
from Diary.models import DiaryGroup
from ..permissions import IsSelf
from rest_framework.response import Response

from Diary.serializers.diary_sz import DiarySZ
from Diary.serializers.diary_sz import DiaryDetailSZ
from Diary.serializers.diary_sz import DiaryMeSZ

from Diary.serializers.diary_member_sz import DiaryMemberSZ
from Diary.serializers.diary_member_sz import DiaryMemberMeSZ
from Diary.serializers.diary_member_withdrawl_sz import DiaryMemberWithdrawlSZ
from rest_framework import status

from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView

from ..exceptions.now_writer_not_withdrawl import NowWriterNotWithdrwal
from ..tasks import add


class DiaryMemberDetailWithdrawl(RetrieveDestroyAPIView):
    queryset = DiaryMember.objects.all()
    serializer_class = DiaryMemberWithdrawlSZ

    def get_queryset(self):
        return DiaryMember.objects.filter(diary_id=self.kwargs.get('diary_pk'), user=self.request.user)

    def get_object(self):
        return get_object_or_404(DiaryMember, diary_id=self.kwargs.get('diary_pk'), user=self.request.user)

    def delete(self, request, *args, **kwargs):
        diary = get_object_or_404(Diary, id=self.kwargs.get('diary_pk'))
        if diary.now_writer == self.request.user:
            raise NowWriterNotWithdrwal()
        self.get_object().delete() # TODO: 알림 보내야댐
        return Response(status=status.HTTP_200_OK, data='OK')
