from rest_framework import serializers
from .models import Todo, TodoList

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'text', 'checked', 'notes', 'todo_list')
        
class TodoListSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True)
    class Meta:
        model = TodoList
        fields = ('firebase_uid', 'todos')