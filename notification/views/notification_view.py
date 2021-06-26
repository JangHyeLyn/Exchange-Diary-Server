from rest_framework import status

from rest_framework.response import Response

from notification.models import Notification
from notification.serializers.notification_list_sz import NotificationListSZ
from rest_framework.generics import ListAPIView


class NotificatoinListView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationListSZ

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)[:20]

    def get(self, request, *args, **kwargs):
        serializer_data = self.get_serializer(self.get_queryset(), many=True).data

        return Response(status=status.HTTP_200_OK, data=serializer_data)
