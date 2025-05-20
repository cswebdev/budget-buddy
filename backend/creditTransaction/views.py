from rest_framework import viewsets
from .serializers import CreditTransactionSerializer
from .models import CreditTransaction


class CreditTransactionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the CreditTransaction model.
    """

    serializer_class = CreditTransactionSerializer

    def get_queryset(self):
        return CreditTransaction.objects.all()
    
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
 
