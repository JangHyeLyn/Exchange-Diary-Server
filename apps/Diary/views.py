from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Diary
from .serializers.user_diary_set_sz import UserDiarySetSZ


class DiaryViewSet(ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = UserDiarySetSZ
    permission_classes = [IsAuthenticated]