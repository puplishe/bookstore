from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]
    def perform_create(self, serializer: UserSerializer):
        user = serializer.save()
        return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)