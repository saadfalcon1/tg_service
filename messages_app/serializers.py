from rest_framework import serializers
from .models import TelegramMessage


class TelegramMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramMessage
        fields = ('id', 'recipient_id', 'text', 'sent_at', 'status')
        read_only_fields = ('id', 'sent_at', 'status')


class TelegramMessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramMessage
        fields = ('id', 'recipient_id', 'text', 'sent_at', 'status')
