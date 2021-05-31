from rest_framework import serializers
from .models import *

class TrainerSerializer(serializers.ModelSerializer):
    # profice_pic = serializers.ImageField(max_length=None,allow_empty_file=False,allow_null=True,required=False)
    class Meta:
        model = Teacher
        fields = ["id","name","gender","phone","profice_pic","qualification"]


