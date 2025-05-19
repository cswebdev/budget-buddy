from django.db import models

'''
This model is used to detail user bank accounts.
'''

class Account(models.Model):
    """
    This model is used to detail user bank accounts.
    """

    # The name of the account
    account_name = models.CharField(max_length=255)

    # The balance of the account
    balance = models.DecimalField(max_digits=10, decimal_places=2)


    # The date the account was last updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
