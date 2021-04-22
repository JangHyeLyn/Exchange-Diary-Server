from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..models import DiaryGroup

from ..serializers.diary_group_sz import DiaryGroupSZ, DiaryGroupCreateSZ
from ..serializers.diary_group_member_sz import DiaryGroupMemberSZ

from django.db import transaction

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

class ListCreateDiaryGroupView(generics.ListCreateAPIView):
    queryset = DiaryGroup.objects.all()
    serializer_class = DiaryGroupCreateSZ

    def get_queryset(self):
        return DiaryGroup.objects.filter(user=self.request.user)

    # def list(self, request, *args, **kwargs):
    #     serializer = self.get_serializer()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(user=request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

