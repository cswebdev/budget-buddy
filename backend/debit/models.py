from django.db import models

'''
This model is used to detail debit transactions.
'''
class Debit(models.Model):
    """
    This model is used to detail debit transactions.
    """

    # The amount of the debit
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # The date of the debit
    date = models.DateField()

    # The description of the debit
    description = models.CharField(max_length=255)

    # The account associated with the debit
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} - {self.date} - {self.description}"