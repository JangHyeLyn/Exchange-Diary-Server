from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from django.contrib.auth import get_user_model


class UserDiaryMemberSZ(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', ]
