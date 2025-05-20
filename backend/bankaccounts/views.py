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
    
    def perform_create(self, serializer):
        """
        Override the perform_create method to add custom logic.
        """
        # Add custom logic here if needed
        serializer.save()
    def perform_update(self, serializer):
        """
        Override the perform_update method to add custom logic.
        """
        # Add custom logic here if needed
        serializer.save()

    def perform_destroy(self, instance):
        """
        Override the perform_destroy method to add custom logic.
        """
        # Add custom logic here if needed
        instance.delete()
