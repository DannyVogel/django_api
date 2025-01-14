from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import StudentSerializer
from .models import Student

class TestView(APIView): 
    def get(self, request):
        qs = Student.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'statusCode': 200,
            "message": "Student data created successfully",
            "data":serializer.data})