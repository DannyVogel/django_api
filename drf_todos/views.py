from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import TodoSerializer, TodoListSerializer
from .models import Todo, TodoList
# Create your views here.
class TodoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, firebase_uid, todo_id=None):
        if todo_id:
            qs = Todo.objects.filter(todo_list__firebase_uid=firebase_uid, id=todo_id)
        else:
            qs = Todo.objects.filter(todo_list__firebase_uid=firebase_uid)
        serializer = TodoSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, firebase_uid): 
        todo_list, created = TodoList.objects.get_or_create(firebase_uid=firebase_uid)
        
        data = request.data.copy()
        data['todo_list'] = todo_list.id
        
        serializer = TodoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, firebase_uid, todo_id):
        qs = Todo.objects.filter(todo_list__firebase_uid=firebase_uid, id=todo_id)
        qs.delete()
        return Response({"message": "Todo deleted successfully"})

    def patch(self, request, firebase_uid, todo_id):
        try:
            todo = Todo.objects.get(
                id=todo_id, 
                todo_list__firebase_uid=firebase_uid
            )
            
            todo.checked = request.data.get('checked', todo.checked)
            todo.save()
            
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
            
        except Todo.DoesNotExist:
            return Response(
                {"error": "Todo not found"}, 
                status=404
            )
