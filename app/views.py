from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class UserSignUpView(APIView):

    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'status':'success'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)


class UserSignInView(APIView):

    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username = username,password = password)
        if user:
            token = RefreshToken.for_user(user)
            serializer = UserSerializer(user)
            return Response({
                'status':'success',
                'user': serializer.data,
                'refresh': str(token),
                'access': str(token.access_token)
            })
        return Response({'status':'error'},status=status.HTTP_401_UNAUTHORIZED)

