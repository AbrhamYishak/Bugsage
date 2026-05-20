from django.shortcuts import render
from rest_framework import generics
from .models import ErrorCase,ErrorType
from .serializers import ErrorCaseSerializer, ErrorTypeSerializer
# from rest_framwork.views import APIView
class ErrorTypeView(generics.ListCreateAPIView):
    queryset = ErrorType.objects.all()
    serializer_class = ErrorTypeSerializer
class ErrorCaseView(generics.ListCreateAPIView):
    queryset = ErrorCase.objects.all()
    serializer_class = ErrorCaseSerializer
# class Error(APIView):
#     def get(self,request):

# Create your views here.
