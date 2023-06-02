from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Task
from base.serializers import TaskSerializer,RegisterSerializer,LoginSerializer

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Class Based API View


class RegisterAPI(APIView):

    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data = data)

        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':serializer.errors
            } , status.HTTP_400_BAD_REQUEST)
        serializer.save()

        return Response({'status': True,'message':'user created'},status.HTTP_201_CREATED)


class LoginAPI(APIView):

    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':serializer.errors
            } , status.HTTP_400_BAD_REQUEST)
        user = authenticate(username = serializer.data['username'],
                            password = serializer.data['password'])
        if not user:
            return Response({
                'status':False,
                'message':'invalid credentials'
            } , status.HTTP_400_BAD_REQUEST)
        
        token,_ = Token.objects.get_or_create(user = user)

        return Response({'status': True,'message':'user login','token': str(token)},status.HTTP_201_CREATED)

class TaskAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    # GET method
    def get(self, request):
        print(request.user)
        objs = Task.objects.all()
        serializer = TaskSerializer(objs,many = True)
        return Response(serializer.data)

    # POST method
    def post(self, request):
        data  = request.data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    # PUT method
    def put(self, request):
        data = request.data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    # PATCH method
    def patch(self, request):
        data = request.data
        obj = Task.objects.get(id = data['id'])
        serializer = TaskSerializer(obj, data=data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        data = request.data
        obj = Task.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'person deleted'})


##########################################
