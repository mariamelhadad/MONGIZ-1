from django.shortcuts import render
from rest_framework.views import  APIView
from  rest_framework.response import Response
from rest_framework import status
from .serialization import *
# Create your views here.
class Personal_Info(APIView):
    def post (self,request):
        data=request.data
        serialize=PersonalInfoserialization(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({"msg":serialize.data},status=status.HTTP_200_OK)
        else:
            return Response (serialize.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
class Expereince(APIView):
    def post (self,request):
        data=request.data
        serialize=Expereinceserialization(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({"msg":serialize.data},status=status.HTTP_200_OK)
        else:
            return Response (serialize.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
class Technical_Skills(APIView):
    def post (self,request):
        data=request.data
        serialize=Technicalskillsserialization(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({"msg":serialize.data},status=status.HTTP_200_OK)
        else:
            return Response (serialize.errors,status=status.HTTP_400_BAD_REQUEST)
class Education(APIView):
    def post (self,request):
        data=request.data
        serialize=Educationserialization(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({"msg":serialize.data},status=status.HTTP_200_OK)
        else:
            return Response (serialize.errors,status=status.HTTP_400_BAD_REQUEST)
      
        
        
class Contact_Info(APIView):
    def post (self,request):
        data=request.data
        serialize=Contact_Infoserialization(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({"msg":serialize.data},status=status.HTTP_200_OK)
        else:
            return Response (serialize.errors,status=status.HTTP_400_BAD_REQUEST)