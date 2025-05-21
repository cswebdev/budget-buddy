"""
bankaccounts/Serializers for the bank accounts module.
"""

from rest_framework import serializers
from .models import BankAccount
from django.db.models import Sum


class BankAccountSerializer(serializers.ModelSerializer):
    """
    Serializer for the BankAccount model.
    """

    total_credit = serializers.SerializerMethodField()
    total_debit = serializers.SerializerMethodField()
    number_of_credit_transactions = serializers.SerializerMethodField()
    number_of_debit_transactions = serializers.SerializerMethodField()

    class Meta:
        model = BankAccount
        fields = "__all__"
        extra_fields = (
            "total_credit",
            "total_debit",
            "number_of_credit_transactions",
            "number_of_debit_transactions",
        )

    def get_total_credit(self, obj):
        # Use related_name if set, otherwise use credittransaction_set
        return obj.credit_transactions.aggregate(total=Sum("amount"))["total"] or 0

    def get_number_of_credit_transactions(self, obj):
        # Use related_name if set, otherwise use credittransaction_set
        return obj.credit_transactions.count()

    def get_total_debit(self, obj):
        # Use related_name if set, otherwise use debittransaction_set
        return obj.debit_transactions.aggregate(total=Sum("amount"))["total"] or 0

    def get_number_of_debit_transactions(self, obj):
        # Use related_name if set, otherwise use debittransaction_set
        return obj.debit_transactions.count()

    def get_balance(self, obj):
        """
        Calculate the balance of the bank account.
        """
        return self.get_total_credit(obj) - self.get_total_debit(obj)
