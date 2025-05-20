from rest_framework import serializers
from .models import DebitTransaction

class DebitTransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for the DebitTransaction model.
    """

    class Meta:
        model = DebitTransaction
        fields = "__all__"