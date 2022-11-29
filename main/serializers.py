from rest_framework import serializers, exceptions
from .models import *

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    def validate_password(self,value):
        if len(value) < 8:
            raise exceptions.ValidationError('пароль меньше 8 символов')
        elif len(value) > 32:
            raise exceptions.ValidationError('пароль больше 32 символов')
        return value


class AutorisationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

