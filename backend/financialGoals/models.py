from django.db import models
from user.models import User

"""
This model is used to detail a user's financial goals. A financial goal is a goal that the user wants to achieve with their money.
"""


class FinancialGoal(models.Model):
    """
    This model is used to detail a user's financial goals.
    """

    GOAL_TYPES = [
        ("Savings", "Savings"),
        ("Investment", "Investment"),
        ("Debt Repayment", "Debt Repayment"),
        ("Other", "Other"),
    ]
    STATUS_CHOICES = [
        ("Not Started", "Not Started"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]
    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]
    FREQUENCY_CHOICES = [
        ("One-time", "One-time"),
        ("Monthly", "Monthly"),
        ("Quarterly", "Quarterly"),
        ("Yearly", "Yearly"),
    ]

    """ 
    IMPORTANT: Add AUTH_USER_MODEL later. This is using a basic User model for now.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="financial_goals",
    )
    bank_account = models.ForeignKey(
        "bankAccount.BankAccount",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="financial_goals",
    )
    goal_type = models.CharField(max_length=50, choices=GOAL_TYPES, default="Other")
    name = models.CharField(max_length=255, default="Financial Goal")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    target_date = models.DateTimeField()
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="Not Started"
    )
    priority = models.CharField(
        max_length=50, choices=PRIORITY_CHOICES, default="Medium"
    )
    frequency = models.CharField(
        max_length=50, choices=FREQUENCY_CHOICES, default="One-time"
    )
    is_recurring = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    @property
    def progress(self):
        if self.target_amount:
            return round((self.current_amount / self.target_amount) * 100, 2)
        return 0.0

    def __str__(self):
        return f"{self.bank_account} - {self.name} - {self.target_amount} - {self.target_date}"
