from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.serializers import UserSerializer, PerformanceSerializer, StudentSerializer, StudentExtraSerializer, TeacherSerializer, TeacherExtraSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BasicAuthentication
import jwt, datetime
from django.core.serializers.json import DjangoJSONEncoder
import  json

# Create your views here.

# Function Based Auth Views

@api_view(['POST'])
def login(request):
    
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"Detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

@api_view(['POST'])
def signup(request):
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save() 
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def tokenTest(request):
    user_email = request.user.email
    return Response(f"{user_email} Passed Authentication!")

@api_view(['POST'])
def studentSignup(request):
    serializer = StudentSerializer(data=request.data)
    extraSerializer = StudentExtraSerializer(data=request.data)
    
    if serializer.is_valid() and extraSerializer.is_valid():
        serializer.save()
        student = User.objects.all().filter(request.data['username'])
        student.set_password(request.data['password'])
        student.save()
        serialTwo = extraSerializer.save(commit=False)
        serialTwo.user = student
        serialTwo.save()
        
        studentGroup = Group.objects.get_or_create("STUDENT")
        studentGroup[0].user_set.add(student)
        
        
        return Response({"Success": "Student Added Successfully"})
    return Response(serializer.errors, extraSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def performance(request, pk):
    serializer = PerformanceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(id = pk, username=request.data['student'])
        authenticate_ = tokenTest(user)
        if authenticate_.IsAuthenticated == True:
            return Response({"Student Performance": serializer.data})
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Class Based Auth Views
class Register(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        
class Login(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        
        data = {
            'username' : request.data['username'],
            'password' : request.data['password']
        }
        
        password_ = data['password']
        username_ = data['username']
        print(username_, password_)
        
        user = User.objects.filter(username = username_)
        
        if user is None:
            return AuthenticationFailed({"Error": "User Not Found"})
        if password_ is None:
            return AuthenticationFailed({"Error": "Incorrect Password"})
        
        dateTime = datetime.datetime.utcnow()
        deltaTime = datetime.timedelta(minutes=60)
        serialized_datetime = json.dumps(dateTime, cls=DjangoJSONEncoder)
        serialized_delta_time = json.dumps(deltaTime, cls=DjangoJSONEncoder)
        
        payload = {
            'username': username_,
            'token_created': serialized_datetime,
            'expiry_time' : serialized_datetime + serialized_delta_time
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='Token', value=token, expires=payload['expiry_time'], httponly=True)
        
        response.data = {
            'Token': token,
            'Created On': payload['token_created'],
            'Expires In': payload['expiry_time']
        }
        return response 

class CredentialChecker(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        
        token = request.COOKIES.get('Token')
        
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        
        while token:
            try:
                data = jwt.decode(token, 'secret', algorithms=["HS256"])
                return Response(data)
            except:
                return Response({"Error": "Token Invalid"})
                
        if request.user:
            try:
                user = User.objects.get(username=request.data["username"])
                return Response({f"{user}": f"{user.password}", f"{user.email}": f"{content}"})
            except:
                return Response({"error": "user invalid"})
            

class Logout(APIView):
    def post(self, request, format=None):
        response = Response()
        response.delete_cookie('Token')
        response.data = {
            'message': 'Logged Out Successfully!'
        }
        
        return response
    
    
