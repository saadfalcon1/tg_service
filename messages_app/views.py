from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import TelegramMessage
from .serializers import TelegramMessageSerializer, TelegramMessageListSerializer
from telegram_bot.bot import send_telegram_message


class SendMessageView(generics.CreateAPIView):
    serializer_class = TelegramMessageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        message = serializer.save(user=self.request.user)
        success = send_telegram_message(message.recipient_id, message.text)
        if success:
            message.status = 'delivered'
        else:
            message.status = 'failed'
        message.save()


class MessageHistoryView(generics.ListAPIView):
    serializer_class = TelegramMessageListSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return TelegramMessage.objects.filter(user=self.request.user).order_by('-sent_at')
