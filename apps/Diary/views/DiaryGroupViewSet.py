from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import DiaryGroup
from rest_framework.decorators import action
from rest_framework.response import Response
from ..serializers.diary_group_sz import DiaryGroupSZ, DiaryGroupCreateSZ
from ..serializers.diary_group_member_sz import DiaryGroupMemberSZ

from django.db import transaction
from rest_framework import status


class DiaryGroupViewSet(ModelViewSet):
    queryset = DiaryGroup.objects.all()
    serializer_class = DiaryGroupSZ
    tags = ["Group"]

    def get_queryset(self):
        return DiaryGroup.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(data=serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = DiaryGroupCreateSZ(data=request.data)
        serializer.is_valid(raise_exception=True)

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
