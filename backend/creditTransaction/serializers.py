"""
creditTransaction/serializers.py
Serializers for recording bank account module credit transactions.
"""

from rest_framework import serializers
from .models import CreditTransaction


class CreditTransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for the CreditTransaction model.
    """

    class Meta:
        model = CreditTransaction
        fields = "__all__"


""" 
Will add custom logic and validation here later.
"""
