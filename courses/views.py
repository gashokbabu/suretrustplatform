from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from trainer.permissions import TrainerAccessPermission,ReadOnly
class CourseViewset(viewsets.ModelViewSet):
    permission_classes=[TrainerAccessPermission|ReadOnly]
    serializer_class = CourseSerializer
    def get_queryset(self):
        return Course.objects.filter(batch__teacher__user=self.request.user).distinct()

class BatchViewset(viewsets.ModelViewSet):
    permission_classes=[TrainerAccessPermission|ReadOnly]
    serializer_class = BatchSerializer
    def get_queryset(self):
        user = self.request.user
        course_name = self.request.data['course_name']
        return Batch.objects.filter(teacher__user=self.request.user,course=course_name)

class PostViewset(viewsets.ModelViewSet):
    permission_classes=[TrainerAccessPermission|ReadOnly]
    serializer_class = PostSerializer
    def get_queryset(self):
        print(self.request.data)
        return Post.objects.filter(batch__teacher__user=self.request.user,batch__id=1).order_by('date_time')


def studentsOfBatch(request):
    pass


