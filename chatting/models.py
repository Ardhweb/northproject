from django.contrib.auth.models import User
from django.db import models



class ChatThread(models.Model):
    room_name = models.CharField(max_length=500)
    origin_user = models.IntegerField()
    other_user = models.IntegerField()
    active = models.BooleanField(default=True)
    class Meta:
        unique_together = ('origin_user', 'other_user')

    # def __str__(self):
    #     return f"Chat between {self.alpha_user.username} and {self.beta_user.username}"

class ChatText(models.Model):
    thread = models.ForeignKey(ChatThread, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"Message from {self.sender.username} at {self.timestamp}"
