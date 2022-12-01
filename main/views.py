from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from .models import *
from .serializers import *
from .email import message
User = get_user_model()


class RegistrationView(APIView):
    def post(self, request):
        serializer  = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        if User.objects.filter(username=username).exists():
            return Response({'message':'User already exists'})
        user = User.objects.create_user(
            username=username,
            email=email,
            password = password
        )
        message(email)
        # user.set_password(password)
        # user.save
        token = Token.objects.create(user=user)
        return Response({'token': token.key})
        # token = Token.objects.create(password=password)


class AutorisationView(APIView):


    def post(self, request):
        serializer = AutorisationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username=username).first()
        if user is not None:
            if check_password(password, user.password):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=200)
            return Response({'error': 'Invalid password '}, status=400)
        return Response({'error': 'No such a user'}, status=400)

        



