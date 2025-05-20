"""
bankaccounts/Serializers for the bank accounts module.
"""

from rest_framework import serializers
from .models import BankAccount


class BankAccountSerializer(serializers.ModelSerializer):
    """
    Serializer for the BankAccount model.
    """

    class Meta:
        model = BankAccount
        fields = "__all__"
