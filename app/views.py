from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import authentication
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

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
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
