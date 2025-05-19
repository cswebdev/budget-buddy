from django.db import models

# Create your models here.
'''
This model is used to detail deposit transactions.
'''

class Deposit(models.Model):
    """
    This model is used to detail deposit transactions.
    """

    # The amount of the deposit
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # The date of the deposit
    date = models.DateField()

    # The description of the deposit
    description = models.CharField(max_length=255)

    # The account associated with the deposit
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} - {self.date} - {self.description}"