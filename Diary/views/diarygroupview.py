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
from ..serializers.diary_group_member_sz import DiaryGroupMemberSZ

from django.db import transaction


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
        return Response(data=serializer.data)

    @action(detail=True, methods=['get'], url_path='members')
    def member(self, request, pk):
        members = self.get_object().members.all()
        serializer = DiaryGroupMemberSZ(members, many=True)

        return Response(data=serializer.data)

    @member.mapping.post
    def create_member(self, request, pk):
        diary_list = request.data.get('diary_list')
        print(diary_list)
        return Response(data=None)

    @member.mapping.delete
    def delete_member(self, request, pk):
        pass


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
        DiaryGroup.group_rank_update(data=request.data)
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
        serializer = DiaryGroupRetriveSZ(self.get_queryset().get(pk=kwargs['pk']))
        data = dict(
            diary_group=serializer.data
        )
        return Response(data=data)

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)