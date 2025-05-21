from django.db import models
from bankaccounts.models import BankAccount


class DebitTransaction(models.Model):
    """
    This model is used to detail a users bank account debit transaction(s). A debit transaction is a transaction that removes money from the users bank account.
    """

    DEBIT_CATEGORIES = [
        ("Groceries", "Groceries"),
        ("Rent", "Rent"),
        ("Utilities", "Utilities"),
        ("Entertainment", "Entertainment"),
        ("Other", "Other"),
    ]

    # Foreign key to the bank account model
    bank_account = models.ForeignKey(
        BankAccount, on_delete=models.CASCADE, related_name="debit_transactions"
    )

    # The name of the transaction
    transaction_name = models.CharField(max_length=255, default="Debit Transaction")

    # The amount of the transaction
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # The category of the transaction
    category = models.CharField(
        max_length=50, choices=DEBIT_CATEGORIES, default="Other"
    )

    # The date of the transaction
    transaction_date = models.DateTimeField()

    def __str__(self):
        return f"{self.bank_account} - {self.amount} - {self.transaction_date}"
