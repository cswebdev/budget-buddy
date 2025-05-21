from .serializers import UserSerializer
from rest_framework import viewsets
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the User model.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
