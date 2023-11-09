from rest_framework import serializers
from django.contrib.auth.models import User
from paytask.models import Performance

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']


#Performance Serializer
class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ['user', 'subject', 'grade']