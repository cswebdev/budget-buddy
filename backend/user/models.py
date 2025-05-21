from django.db import models


class User(models.Model):
    """
    Extremely basic User model for the application. No current validation.
    No current authentication. No current permissions.
    This model is used to detail a users bank account(s).
    Will create authentication and permissions in the future.
    """

    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)
    linked_bank_accounts = models.ManyToManyField(
        "bankaccounts.BankAccount", related_name="users", blank=True
    )

    def __str__(self):
        return self.username
