from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import ErrorCase,ErrorType
from .serializers import ErrorCaseSerializer, ErrorTypeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framwork.views import APIView
class ErrorTypeView(generics.ListCreateAPIView):
    queryset = ErrorType.objects.all()
    serializer_class = ErrorTypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['errorType']
class ErrorCaseView(generics.ListCreateAPIView):
    queryset = ErrorCase.objects.all()
    serializer_class = ErrorCaseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['caseName']
@api_view(['POST'])
def upvote(request,pk):
    errorType = ErrorType.objects.get(pk=pk)
    errorType.upVotes+=1
    errorType.save()
    return Response({"message":"Upvoted"},status = 200)
@api_view(['POST'])
def downvote(request,pk):
    errorType = ErrorType.objects.get(pk=pk)
    errorType.downVotes+=1
    errorType.save()
    return Response({"message":"Downvoted"},status = 200)
# class Error(APIView):
#     def get(self,request):

# Create your views here.
