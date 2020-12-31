from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from ..models import Diary
from ..serializers.diary_list_sz import DiaryListSZ, DiaryDetailSZ


class DiaryVS(ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiaryListSZ
    permission_classes = [IsAuthenticated]

    # def list(self, request):
    #     queryset = Diary.objects.all()
    #     serializer = DiaryListSZ(queryset, many=True)
    #     return Response(serializer.data)
    #
    def retrieve(self, request, pk=None):
        print("# retrieve #")
        queryset = Diary.objects.all()
        diary = get_object_or_404(queryset, pk=pk)
        print(diary.user.id)
        serializer = DiaryDetailSZ(diary)
        return Response(serializer.data)
