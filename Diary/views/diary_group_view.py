from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..models import DiaryGroup

from ..serializers.diary_group_sz import DiaryGroupListSZ
from ..serializers.diary_group_sz import DiaryGroupRetriveSZ
from ..serializers.diary_group_sz import DiaryGroupCreateSZ
from ..serializers.diary_group_sz import DiaryGroupUpdateDeleteSZ
from ..serializers.diary_sz import DiaryInGroupSZ
# from ..serializers.diary_group_member_sz import DiaryGroupMemberSZ

from django.db import transaction
from django.shortcuts import get_object_or_404

class DiaryGroupViewSet(ModelViewSet):
    queryset = DiaryGroup.objects.all()
    serializer_class = DiaryGroupListSZ
    tags = ["Group"]

    def get_queryset(self):
        return DiaryGroup.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(data=serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = DiaryGroupCreateSZ(self.get_queryset(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class DiaryGroupListCreateUpdateView(ListCreateAPIView, UpdateAPIView):
    queryset = DiaryGroup.objects.all()
    serializer_class = DiaryGroupCreateSZ
    permission_classes = (
        IsAuthenticated,
    )

    def get_queryset(self):
        return DiaryGroup.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        serializer = DiaryGroupListSZ(self.get_queryset(), many=True)
        data = dict(
            not_join_group_cnt=DiaryGroup.not_join_group_count(user=request.user),
            diary_groups=serializer.data
        )
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED,
                        headers=self.get_success_headers(serializer.data))

    def patch(self, request, *args, **kwargs):
        DiaryGroup.group_rank_update(datas=request.data)
        serializer = DiaryGroupListSZ(self.get_queryset(), many=True)
        data = dict(
            not_join_group_cnt=DiaryGroup.not_join_group_count(user=request.user),
            diary_groups=serializer.data
        )
        return Response(data=data, status=status.HTTP_200_OK)


class DiaryGroupDetailView(RetrieveUpdateDestroyAPIView):
    queryset = DiaryGroup.objects.all()
    serializer_class = DiaryGroupListSZ
    permission_classes = (
        IsAuthenticated,
    )

    def get(self, request, *args, **kwargs):
        diarygroup = get_object_or_404(DiaryGroup, pk=kwargs['pk'])
        diarygroup_serializer = DiaryGroupRetriveSZ(diarygroup)
        diaries_serializer = DiaryInGroupSZ(diarygroup.diaries.all(), many=True)
        data = dict(
            diary_group=diarygroup_serializer.data,
            diaries=diaries_serializer.data
        )
        return Response(data=data)

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)