from django.db import models

"""
This model is used to detail a users bank account credit transaction(s).
"""


class CreditTransaction(models.Model):
    """
    This model is used to detail a users bank account credit transaction(s).
    """

    # Foreign key to the bank account model
    bank_account = models.ForeignKey(
        "bankaccounts.BankAccount", on_delete=models.CASCADE
    )

    # The amount of the transaction
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # The date of the transaction
    transaction_date = models.DateTimeField()

    # The user associated with the transaction
    # user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bank_name} - {self.account_name} - {self.amount} - {self.transaction_date}"
