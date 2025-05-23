from rest_framework import serializers
from .models import DebitTransaction


class DebitTransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for the DebitTransaction model.
    """

    is_past_due = serializers.ReadOnlyField()
    is_recurring_due = serializers.ReadOnlyField()

    class Meta:
        model = DebitTransaction
        fields = "__all__"

    def validate(self, data):
        category = data.get("category")
        subcategory = data.get("subcategory")
        if category and subcategory:
            valid_subcategories = dict(DebitTransaction.SUBCATEGORY_CHOICES).get(
                category, []
            )
            valid_subcategory_values = [choice[0] for choice in valid_subcategories]
            if subcategory not in valid_subcategory_values:
                raise serializers.ValidationError(
                    {
                        "subcategory": f"Invalid subcategory '{subcategory}' for category '{category}'."
                    }
                )
        return data
