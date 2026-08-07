from rest_framework import serializers
from .models import ErrorCase,ErrorType
import re
class ErrorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorType
        fields = ['id','errorType','package','category','severity','generalExplanation','generalFix','docsUrl','upVotes','downVotes','createdByAI','AiModel','fingerPrint']
    def validate(self, attrs):
        if attrs["createdByAI"] and not attrs.get("AiModel"):
            raise serializers.ValidationError(
                "AiModel is required when createdByAI is true."
            )
        return attrs
    def validate_fingerPrint(self, value):
        import re

        if not re.fullmatch(r"[a-f0-9]{64}", value):
            raise serializers.ValidationError(
                "Fingerprint must be a valid SHA-256 hash."
            )

        return value
    def validate_category(self,value):
        category = {"SYNTAX","RUNTIME","LOGIC","NETWORK","DATABASE","AUTH","IMPORT","TYPE","MEMORY","API","UNKNOWN"}
        if value.upper() not in category:
            raise serializers.ValidationError("Unacceptable catagory.")
        return value
    def validate_severity(self,value):
        severity = {"LOW","MEDIUM","HIGH","CRITICAL"}
        if value.upper() not in severity:
            raise serializers.ValidationError("Unacceptable severity.")
        return value
class ErrorCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorCase
        fields = ['caseName','explanation','fix','severity','ErrorTypeID','AiModel','fingerPrint']
    def validate_fingerPrint(self, value):
        import re

        if not re.fullmatch(r"[a-f0-9]{64}", value):
            raise serializers.ValidationError(
                "Fingerprint must be a valid SHA-256 hash."
            )

        return value
    def validate_severity(self,value):
        severity = {"LOW","MEDIUM","HIGH","CRITICAL"}
        if value.upper() not in severity:
            raise serializers.ValidationError("Unacceptable severity.")
        return value