from django.urls import path
from notification.views import NotificationView

urlpatterns = [
    path('notification', NotificationView.as_view(), name='index')
]
