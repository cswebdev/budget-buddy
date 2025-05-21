from rest_framework import serializers
from .models import User
from bankaccounts.models import BankAccount
from bankaccounts.serializers import BankAccountSerializer


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """

    linked_bank_accounts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=BankAccount.objects.all(), required=False
    )
    # Or, for nested details:
    # linked_bank_accounts = BankAccountSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"
