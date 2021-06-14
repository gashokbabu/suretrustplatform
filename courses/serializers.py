from rest_framework import serializers
from .models import *
from trainee.serializers import TraineeSerializer

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    student = TraineeSerializer(read_only=True)
    class Meta:
        model = Grade
        fields = '__all__'

        