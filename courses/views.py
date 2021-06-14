from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from trainer.permissions import TrainerAccessPermission,ReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from trainee.serializers import TraineeSerializer
from rest_framework.parsers import FileUploadParser
class CourseViewset(viewsets.ModelViewSet):
    permission_classes=[TrainerAccessPermission|ReadOnly]
    serializer_class = CourseSerializer
    pagination_class=None
    def get_queryset(self):
        if self.request.user.is_staff:
            return Course.objects.filter(batch__teacher__user=self.request.user).distinct()
        else:
            return Course.objects.filter(batch__students=self.request.user.student).distinct()

class BatchViewset(viewsets.ModelViewSet):
    permission_classes=[TrainerAccessPermission|ReadOnly]
    serializer_class = BatchSerializer
    pagination_class=None
    def get_queryset(self):
        user = self.request.user
        course_id = self.request.headers['course-id']
        course_id = int(course_id)
        if self.request.user.is_staff:
            return Batch.objects.filter(teacher__user=self.request.user,course__id=course_id)
        else:
            return Batch.objects.filter(batch__students=self.request.user.student,course=course_id)
class PostViewset(viewsets.ModelViewSet):
    permission_classes=[TrainerAccessPermission|ReadOnly]
    serializer_class = PostSerializer
    pagination_class=PageNumberPagination
    def get_queryset(self):
        if self.request.user.is_staff:
            batch_id = self.request.headers['batch-id']
            return Post.objects.get(batch__teacher__user=self.request.user,batch__id=batch_id).order_by('-date_time')
        else:
            course_id = self.request.headers['course-id']
            batch_id = Batch.objects.filter(students__user=self.request.user)[0]
            print(batch_id)
            return Post.objects.filter(batch__students=self.request.user.student,batch=batch_id).order_by('-date_time')
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        if serializer.data['type'].lower() == 'assignment':
            post = Post.objects.get(id=serializer.data['id'])
            batch1 = Batch.objects.get(id=serializer.data['batch'])
            students = batch1.students.all()
            print(students)
            for student1 in students:
                g = Grade(student=student1,post=post)
                g.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class GradeViewSet(viewsets.ModelViewSet):
    pagination_class = None
    permission_classes=[TrainerAccessPermission|ReadOnly]
    serializer_class = GradeSerializer
    def get_queryset(self):
        user = self.request.user
        post_id = self.request.headers['post-id']
        return Grade.objects.filter(post__id=post_id).order_by('-date')


@api_view(['POST'])
@permission_classes([TrainerAccessPermission])
def studentsOfBatch(request):
    if request.method == 'POST':
        batch_id = request.data['batch_id']
        batch=Batch.objects.get(id=batch_id)
        students = batch.students.all()
        serializer = TraineeSerializer(students,many=True)
        return Response(serializer.data)
    else:
        return Response({'error':'only post request is allowed'})


@api_view(['GET'])
@permission_classes([TrainerAccessPermission])
def assignmentPosts(request):
    batch_id = request.data['batch_id']
    posts = Post.objects.filter(batch__teacher__user=request.user,type='assignment',batch__id=batch_id)
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)





