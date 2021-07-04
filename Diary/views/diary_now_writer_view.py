from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
# Diary
from Diary.models import Diary
from Diary.serializers.diary_now_writer_sz import DiaryNowWriterSZ


class DiaryNowWriterView(ListAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiaryNowWriterSZ

    def get_queryset(self):
        now_diary = Diary.objects.filter(_now_writer=self.request.user)
        return now_diary

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
