from rest_framework import serializers
from discussion.models import discussion_Comment

class  discussion_comment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = discussion_Comment
        fields = ['sno', 'comment', 'user', 'batch', 'parent', 'timestamp']
