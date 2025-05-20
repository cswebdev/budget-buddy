from django.db import models

"""
This model is used to detail a users bank account(s).
"""


class BankAccount(models.Model):
    """
    This model is used to detail a users bank account(s).
    """

    # The name of the bank
    bank_name = models.CharField(max_length=255)

    # The account name
    account_name = models.CharField(max_length=255)

    # The balance of the account
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    # The user associated with the account
    # user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    # The date the account was last updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bank_name} - {self.account_name} - {self.balance}"
