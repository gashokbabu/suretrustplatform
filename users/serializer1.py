from rest_framework import serializers
from .models import User
from trainee.serializers import TraineeSerializer

class UserDummySerializer(serializers.ModelSerializer):
    student = TraineeSerializer()
    class Meta:
        model = User
        extra_kwargs = {'password':{'write_only':True}}
        fields = ('id','email','password','student')