from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import RegisterSerializer, UserProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

class LogoutView(APIView):
    def post(self, request):
        token = RefreshToken(request.data['refresh'])
        token.blacklist()
        return Response({'detail': 'logged out'})

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user