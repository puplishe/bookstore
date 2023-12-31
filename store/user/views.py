from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserSerializer
from .tasks import send_welcome_email


class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]

    def perform_create(self, serializer: UserSerializer):
        user: CustomUser = serializer.save()
        send_welcome_email.delay(user.email)
        return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)
