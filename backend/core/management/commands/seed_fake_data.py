from django.core.management.base import BaseCommand
from faker import Faker
from user.models import User
from bankaccounts.models import BankAccount
from creditTransaction.models import CreditTransaction
import random
from django.utils import timezone

class Command(BaseCommand):
    """
    Django management command to seed the database with fake data for testing purposes.

    This command performs the following actions:
    - Creates 10 fake users with random usernames, emails, and passwords.
    - For each user, creates between 2 and 5 fake bank accounts with random bank names, account names, and balances.
    - For each bank account, creates between 1 and 3 fake credit transactions with random amounts and transaction dates.

    All generated data is associated appropriately between users, bank accounts, and transactions.
    """
    help = 'Seed fake data into the database'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create 10 fake users
        users = []
        for _ in range(10):
            user = User.objects.create(
                username=fake.user_name(),
                password=fake.password()
            )
            users.append(user)

        # For each user, create 2-5 bank accounts and link them
        for user in users:
            for _ in range(random.randint(2, 5)):
                bank_account = BankAccount.objects.create(
                    bank_name=fake.company(),
                    account_name=fake.word().capitalize() + " Account",
                    balance=round(random.uniform(10.00, 10000.00), 2),
                )
                # Link the bank account to the user (ManyToMany)
                user.linked_bank_accounts.add(bank_account)

                # Create 1-3 credit transactions for each bank account
                for _ in range(random.randint(1, 3)):
                    naive_dt = fake.date_time_this_year()
                    aware_dt = timezone.make_aware(naive_dt)
                    CreditTransaction.objects.create(
                        bank_account=bank_account,
                        amount=round(random.uniform(10.00, 500.00), 2),
                        transaction_date=aware_dt,
                    )