from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from django.contrib.auth import get_user_model
from Diary.serializers.user_diary_set_sz import UserDiarySetSZ
from Diary.serializers.now_writer_set_sz import NowWriterSZ


class UserSZ(ModelSerializer):
    diary_set = UserDiarySetSZ(many=True, read_only=True)
    now_writer_set = NowWriterSZ(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email','description','kakao_img', 'diary_set', 'now_writer_set']