from django.db import models
import uuid

class TodoList(models.Model):
    firebase_uid = models.CharField(max_length=128)
    
    def __str__(self):
        return f"Todo List for user {self.firebase_uid}"

class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=100)
    checked = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='todos')
    
    def __str__(self):
        return self.text
