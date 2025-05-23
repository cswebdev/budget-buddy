from rest_framework import serializers
from .models import FinancialGoal


class FinancialGoalSerializer(serializers.ModelSerializer):
    """
    Serializer for the FinancialGoal model.
    """

    total_amount = serializers.SerializerMethodField()
    amount_saved = serializers.SerializerMethodField()
    amount_remaining = serializers.SerializerMethodField()
    percentage_saved = serializers.SerializerMethodField()

    class Meta:
        model = FinancialGoal
        fields = "__all__"

    def get_total_amount(self, obj):
        """
        Calculate the total amount of the financial goal.
        """
        return obj.target_amount
        # Assuming target_amount is the total amount for the goal

    def get_amount_saved(self, obj):
        """
        Calculate the amount saved towards the financial goal.
        """
        return obj.current_amount
        # Assuming current_amount is the amount saved so far

    def get_amount_remaining(self, obj):
        """
        Calculate the amount remaining to reach the financial goal.
        """
        return obj.target_amount - obj.current_amount
        # Assuming target_amount is the total amount and current_amount is the amount saved so far

    def get_percentage_saved(self, obj):
        """
        Calculate the percentage saved towards the financial goal.
        """
        if obj.target_amount > 0:
            return round((obj.current_amount / obj.target_amount) * 100, 2)
        return 0
        # Assuming target_amount is the total amount and current_amount is the amount saved so far

    def validate(self, data):
        """
        Validate the financial goal data.
        """
        if data.get("target_amount") <= 0:
            raise serializers.ValidationError(
                {"target_amount": "Target amount must be greater than zero."}
            )
        if data.get("current_amount") < 0:
            raise serializers.ValidationError(
                {"current_amount": "Current amount cannot be negative."}
            )
        return data
