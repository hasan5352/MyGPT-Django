import uuid
from django.db import models
from users.models import User

# Create your models here.
class Thread(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(default="New Chat")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)            # updated on instance.save()

    def __str__(self):
        return f"title: {self.title}. id: {self.id}. user_id: {self.user_id}"
    

class Message(models.Model):
    role_choices = [('user', 'user'), ('robot', 'robot')]
    
    role = models.CharField(max_length=5, choices=role_choices)
    content = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)            # updated on instance.save()

    def __str__(self):
        return f"role: {self.role}. thread_id: {self.thread_id}"
