from rest_framework import serializers
from .models import Student,ContactUs

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'