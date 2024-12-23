from django.urls import path
from .views import SendMessageView, MessageHistoryView

urlpatterns = [
    path('send/', SendMessageView.as_view(), name='send-message'),
    path('history/', MessageHistoryView.as_view(), name='message-history'),
]

