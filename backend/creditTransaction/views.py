""" 
viewSet for the CreditTransaction model.
"""

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
