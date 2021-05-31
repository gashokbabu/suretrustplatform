from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

class TraineeViewset(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = TraineeSerializer

    def create(self, request, *args, **kwargs):
        request.data['registration_no'] = 21
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)