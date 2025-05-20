from .serializers import BankAccountSerializer
from .models import BankAccount
from rest_framework import viewsets


class BankAccountViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the BankAccount model.
    """

    serializer_class = BankAccountSerializer

    def get_queryset(self):
        return BankAccount.objects.all()
