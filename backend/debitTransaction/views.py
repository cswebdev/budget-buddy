from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import DebitTransaction
from .serializers import DebitTransactionSerializer


class DebitTransactionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the DebitTransaction model.
    """

    serializer_class = DebitTransactionSerializer

    def get_queryset(self):
        bankaccount_pk = self.kwargs.get("bankaccount_pk")
        if bankaccount_pk:
            return DebitTransaction.objects.filter(bank_account_id=bankaccount_pk)
        return DebitTransaction.objects.all()

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

    @action(detail=False, methods=["get"])
    def past_due(self, request, *args, **kwargs):
        bankaccount_pk = self.kwargs.get("bankaccount_pk")
        queryset = self.get_queryset().filter(
            category__in=["Bills", "Loans", "Utilities"],
            transaction_date__lt=timezone.now(),
            is_recurring=False,
        )
        if bankaccount_pk:
            queryset = queryset.filter(bank_account_id=bankaccount_pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
