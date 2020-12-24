from rest_framework import generics
from .serializers import SignUpSerializer

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    queryset = UserModel.objects.all()
