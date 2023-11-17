from rest_framework import serializers
from django.contrib.auth.models import User
from paytask.models import Performance, Student, Teacher

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']
        
# Teacher Seralizer

class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        models = User
        fields = ['first_name', 'last_name', 'username', 'password']
        

# Teacher Extra Serializer       
class TeacherExtraSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        models = Teacher
        fields = ['phone', 'joindate', 'salary', 'status']

# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        
# Student Extra Serializer

class StudentExtraSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = Student
        fields = ['phone', 'fee', 'cl', 'roll', 'status']

#Performance Serializer
class PerformanceSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Performance
        fields = ['student', 'subject', 'grade']