from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Diary
from .serializers.diary_list_sz import DiaryListSZ


class DiaryViewSet(ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiaryListSZ
    permission_classes = [IsAuthenticated]