from django.urls import path

from notification.views.notification_view import NotificatoinListView
urlpatterns = [
    path('notifications/', NotificatoinListView.as_view(), name='notifications'),
]
