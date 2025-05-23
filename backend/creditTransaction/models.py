from django.db import models

"""
This model is used to detail a users bank account credit transaction(s). A credit transaction is a transaction that adds money to the users bank account
"""


class CreditTransaction(models.Model):
    """
    This model is used to detail a users bank account credit transaction(s).
    """

    CREDIT_CATEGORIES = [
        ("Salary", "Salary"),
        ("Bonus", "Bonus"),
        ("Refund", "Refund"),
        ("Other", "Other"),
    ]

    # Foreign key to the bank account model
    bank_account = models.ForeignKey(
        "bankAccount.BankAccount",
        on_delete=models.CASCADE,
        related_name="credit_transactions",
    )

    # The name of the transaction
    transaction_name = models.CharField(max_length=255, default="Credit Transaction")

    # The amount of the transaction
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # The category of the transaction
    category = models.CharField(
        max_length=50, choices=CREDIT_CATEGORIES, default="Other"
    )

    # The date of the transaction
    transaction_date = models.DateTimeField()

    def __str__(self):
        return f"{self.bank_account} - {self.amount} - {self.transaction_date}"
