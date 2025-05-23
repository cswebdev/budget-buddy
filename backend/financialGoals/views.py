from rest_framework import viewsets
from .models import FinancialGoal
from .serializers import FinancialGoalSerializer

class FinancialGoalViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the FinancialGoal model.
    """

    serializer_class = FinancialGoalSerializer

    def get_queryset(self):
        user_pk = self.kwargs.get("user_pk")
        if user_pk:
            return FinancialGoal.objects.filter(user_id=user_pk)
        return FinancialGoal.objects.all()

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