from django.db import models
from bankaccounts.models import BankAccount

class DebitTransaction(models.Model):
    """
    This model is used to detail a users bank account debit transaction(s).
    """

    # Foreign key to the bank account model
    bank_account = models.ForeignKey(
        BankAccount, on_delete=models.CASCADE, related_name="debit_transactions"
    )

    # The amount of the transaction
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # The date of the transaction
    transaction_date = models.DateTimeField()


    def __str__(self):
        return f"{self.bank_account} - {self.amount} - {self.transaction_date}"
