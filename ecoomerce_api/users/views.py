from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer

# Create your views here.

class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can register
