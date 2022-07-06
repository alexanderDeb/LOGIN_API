from rest_framework import viewsets,permissions
from rest_framework.permissions import IsAuthenticated
from login.models import User

from .serializers import UserSerializer


class userViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()