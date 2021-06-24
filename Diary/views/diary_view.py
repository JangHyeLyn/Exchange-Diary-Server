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
from notification.models import Notification
from ..exceptions.now_writer_not_withdrawl import NowWriterNotWithdrwal
from ..permissions import IsSelf
from rest_framework.response import Response

from Diary.serializers.diary_sz import DiarySZ
from Diary.serializers.diary_sz import DiaryDetailSZ
from Diary.serializers.diary_sz import DiaryMeSZ

from Diary.serializers.diary_member_sz import DiaryMemberSZ
from Diary.serializers.diary_member_sz import DiaryMemberMeSZ

from rest_framework import status

from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView

from ..tasks import add


class DiaryListCreateView(ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySZ

    def get_queryset(self):
        return self.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            diary = serializer.save()
            serializer_data = self.get_serializer(diary).data
            return Response(status=status.HTTP_200_OK, data=serializer_data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class DiaryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiaryDetailSZ
    permission_classes = (
        IsAuthenticated,
    )

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        add.delay()
        return self.update(request, *args, **kwargs)


class DiaryMeListView(ListAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiaryMeSZ

    def get_queryset(self):
        return Diary.objects.filter(user=self.request.user)


class DiaryMemberListCreateView(ListCreateAPIView):
    queryset = DiaryMember
    serializer_class = DiaryMemberSZ

    def get_queryset(self):
        return DiaryMember.objects.filter(diary_id=self.kwargs.get('diary_pk'))

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            diary_member = serializer.save()
            serializer_data = self.get_serializer(diary_member).data
            return Response(status=status.HTTP_200_OK, data=serializer_data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class DiaryMemberMeView(RetrieveUpdateDestroyAPIView):
    queryset = DiaryMember
    serializer_class = DiaryMemberMeSZ

    def get_queryset(self):
        return DiaryMember.objects.filter(diary_id=self.kwargs.get('diary_pk'), user=self.request.user)

    def get_object(self):
        return get_object_or_404(DiaryMember, diary_id=self.kwargs.get('diary_pk'), user=self.request.user)

    def get(self, request, *args, **kwargs):
        serializer_data = self.get_serializer(self.get_object()).data
        return Response(status=status.HTTP_200_OK, data=serializer_data)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @transaction.atomic()
    def delete(self, request, *args, **kwargs):
        diary = get_object_or_404(Diary, id=self.kwargs.get('diary_pk'))
        if diary.now_writer == self.request.user:
            raise NowWriterNotWithdrwal()
        Notification.send_notification(diary, self.request.user, Notification.TEXT.DROP)
        self.get_object().delete()
        return Response(status=status.HTTP_200_OK, data='OK')