from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password':{'write_only':True}}
        fields = ('id','email','password')
    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    def update(self, instance, validated_data):
        for attr,value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)  #we canot save password directly so we are using set_password method
            else:
                setattr(instance,attr,value)  #for remaining things we can use setattr
        instance.save()
        return instance

