from rest_framework import serializers
from .models import ErrorCase,ErrorType
class ErrorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorType
        fields = ['errorType','package','category','severity','generalExplanation','generalFix','docsUrl']
class ErrorCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorCase
        fields = ['caseName','explanation','fix','severity','ErrorTypeID']
