from django.shortcuts import render
from rest_framework import generics
from .models import ErrorCase,ErrorType
from .serializers import ErrorCaseSerializer, ErrorTypeSerializer
class ErrorTypeView(generics.ListCreateAPIView):
    queryset = ErrorType.objects.all()
    serializer_class = ErrorTypeSerializer
class ErrorCaseView(generics.ListCreateAPIView):
    queryset = ErrorCase.objects.all()
    serializer_class = ErrorCaseSerializer
# Create your views here.
