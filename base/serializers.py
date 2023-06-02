from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

# Register Serializer

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    # check whether the user is in the database or not

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError('username is taken')

        if data['email']:
            if User.objects.filter(username = data['email']).exists():
                raise serializers.ValidationError('email is taken')

        return data
    
    def create(self,validated_data):
        user = User.objects.create(username = validated_data['username'],email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data


# Login serializer

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['user','id','title','description','due_date','tags','status']
        # fields ='__all__'
        # depth = 1

