from notification.models import Notification
from notification.serializers.notification_list_sz import NotificationListSZ
from rest_framework.generics import ListAPIView

class NotificatoinListView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationListSZ

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)