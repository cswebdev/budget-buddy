from django.db import models

"""
This model is used to detail a users bank account(s).
"""


class BankAccount(models.Model):
    """
    This model is used to detail a users bank account(s).
    """

    ACCOUNT_TYPES = [
        ("Checking", "Checking"),
        ("Savings", "Savings"),
        ("Credit", "Credit"),
        ("Other", "Other"),
    ]

    # Checking account-specific fields
    account_type = models.CharField(
        max_length=50, choices=ACCOUNT_TYPES, default="Other"
    )
    account_number = models.CharField(max_length=4, unique=True, default="0000")
    bank_name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    # Savings account-specific fields
    # interest_rate = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
    # maturity_date = models.DateTimeField(null=True, blank=True)
    # withdrawal_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # withdrawal_penalty = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Credit card-specific fields
    payment_due_date = models.DateTimeField(null=True, blank=True)
    minimum_payment = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    last_payment_date = models.DateTimeField(null=True, blank=True)
    past_due_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    def is_credit_card(self):
        """
        Check if the account is a credit card.
        """
        return self.account_type == "Credit"

    def __str__(self):
        return f"{self.bank_name} - {self.account_name} - {self.balance}"
