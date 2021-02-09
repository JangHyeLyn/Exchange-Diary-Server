from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import Diary
from rest_framework.response import Response
from ..serializers.diary_list_sz import DiaryListSZ, DiaryDetailSZ
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

    @members.mapping.delete
    def delete_member(self, request, pk):
        """
        TODO::delete 작업 해야됨
        """
        return Response(data=status.HTTP_400_BAD_REQUEST)
