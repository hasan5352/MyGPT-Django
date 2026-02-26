import uuid
from django.db import models
from users.models import User

# Create your models here.
class Thread(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(default="New Chat")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"title: {self.title}. id: {self.id}. user_id: {self.user_id}"
    

class Message(models.Model):
    role_choices = {'user': 'User', 'robot': 'Robot'}
    
    role = models.CharField(choices=role_choices)
    content = models.TextField()
    thread_id = models.ForeignKey(Thread, on_delete=models.CASCADE)

    def __str__(self):
        return f"role: {self.role}. thread_id: {self.thread_id}"
    