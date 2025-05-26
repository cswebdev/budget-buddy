from django.core.management.base import BaseCommand
from bankAccount.models import BankAccount
from creditTransaction.models import CreditTransaction
from debitTransaction.models import DebitTransaction
from financialGoals.models import FinancialGoal
from user.models import User


class Command(BaseCommand):
    """
    Django management command to delete all fake data from the database.

    This command performs the following actions:
    - Deletes all bank accounts, credit transactions, debit transactions, and financial goals.
    - Deletes all users created for testing purposes.
    """

    help = "Delete all fake data from the database"

    def handle(self, *args, **options):
        users = User.objects.all()
        if not users.exists():
            self.stdout.write(self.style.WARNING("No fake data found to delete."))
            return
        # Delete all bank accounts
        BankAccount.objects.all().delete()

        # Delete all credit transactions
        CreditTransaction.objects.all().delete()

        # Delete all debit transactions
        DebitTransaction.objects.all().delete()

        # Delete all financial goals
        FinancialGoal.objects.all().delete()

        # Delete all users created for testing purposes
        User.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Successfully deleted all fake data."))
