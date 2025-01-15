from django.contrib import admin
from django.urls import path, include
from drfapp.views import TestView
from drf_todos.views import TodoView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('', TestView.as_view(), name='test' ),
    path('todos/<str:firebase_uid>', TodoView.as_view(), name='todo' ),
    path('todos/<str:firebase_uid>/<str:todo_id>', TodoView.as_view(), name='todo' ),
    path('api/token/', obtain_auth_token, name='gettoken'),
]
