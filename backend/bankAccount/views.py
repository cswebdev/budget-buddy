from rest_framework import viewsets
from bankAccount.serializers import BankAccountSerializer
from .models import BankAccount


class BankAccountViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the BankAccount model.
    """

    serializer_class = BankAccountSerializer

    def get_queryset(self):
        user_pk = self.kwargs.get("user_pk")
        if user_pk:
            return BankAccount.objects.filter(users__pk=user_pk)
        return BankAccount.objects.all()

    def perform_create(self, serializer):
        user_pk = self.kwargs.get("user_pk")
        bank_account = serializer.save()
        if user_pk:
            bank_account.users.add(user_pk)
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
