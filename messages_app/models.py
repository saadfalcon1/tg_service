from django.db import models
from django.conf import settings

class TelegramMessage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipient_id = models.CharField(max_length=255)
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='sent')

    def __str__(self):
        return f"Message to {self.recipient_id} at {self.sent_at}"

