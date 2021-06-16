from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from discussion.models import discussion_Comment
from discussion.serializers import *
from trainer.serializers import TrainerSerializer
from users.serializers import UserSerializer
class  discussion_comment_Serializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = discussion_Comment
        fields = ['sno', 'comment', 'user', 'batch', 'timestamp']
