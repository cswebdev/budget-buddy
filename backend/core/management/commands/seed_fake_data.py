from django.core.management.base import BaseCommand
from faker import Faker
import requests
from bankAccount.models import BankAccount
from creditTransaction.models import CreditTransaction
from debitTransaction.models import DebitTransaction
from financialGoals.models import FinancialGoal
import random
from django.utils import timezone
from user.models import User


class Command(BaseCommand):
    """
    Django management command to seed the database with fake data for testing purposes.

    This command performs the following actions:
    - Creates 10 fake users with random usernames, emails, and passwords.
    - For each user, creates between 2 and 5 fake bank accounts with random bank names, account names, and balances.
    - For each bank account, creates between 1 and 3 fake credit transactions with random amounts and transaction dates.

    All generated data is associated appropriately between users, bank accounts, and transactions.
    """

    help = "Seed fake data into the database"

    def handle(self, *args, **options):
        fake = Faker()

        bank_accounts = []
        users = []

        for _ in range(10):
            username = fake.user_name()
            password = fake.password()
            user = User.objects.create(username=username, password=password)
            user.save()
            users.append(user)

        # For each user, create 2-5 bank accounts and link them
        for user in users:
            for _ in range(random.randint(2, 5)):
                account_type = random.choice(["Checking", "Savings", "Credit", "Other"])
                bank_account = BankAccount.objects.create(
                    bank_name=fake.company() + " Bank",
                    account_name=fake.word().capitalize() + " Account",
                    balance=round(random.uniform(10.00, 10000.00), 2),
                    account_type=account_type,
                    account_number=fake.unique.random_int(min=1000, max=9999),
                    payment_due_date=(
                        timezone.make_aware(fake.future_datetime())
                        if account_type == "Credit"
                        else None
                    ),
                    minimum_payment=(
                        round(random.uniform(20.00, 200.00), 2)
                        if account_type == "Credit"
                        else None
                    ),
                    last_payment_date=(
                        timezone.make_aware(fake.past_datetime())
                        if account_type == "Credit"
                        else None
                    ),
                    past_due_amount=(
                        round(random.uniform(0, 500.00), 2)
                        if account_type == "Credit"
                        else None
                    ),
                )

                # Link the bank account to the user
                user.linked_bank_accounts.add(bank_account)
                bank_accounts.append(bank_account)

                # Create 1-3 credit transactions for each bank account
                for _ in range(random.randint(1, 3)):
                    naive_dt = fake.date_time_this_year()
                    aware_dt = timezone.make_aware(naive_dt)
                    CreditTransaction.objects.create(
                        bank_account=bank_account,
                        transaction_name=fake.sentence(nb_words=3),
                        amount=round(random.uniform(10.00, 500.00), 2),
                        transaction_date=aware_dt,
                        category=random.choice(
                            ["Salary", "Bonus", "Refund", "Other"]
                        ),  # Adjust to your CREDIT_CATEGORIES
                    )
                # Create 1-3 debit transactions for each bank account
                for _ in range(random.randint(1, 3)):
                    naive_dt = fake.date_time_this_year()
                    aware_dt = timezone.make_aware(naive_dt)
                    category = random.choice(
                        [cat[0] for cat in DebitTransaction.DEBIT_CATEGORIES]
                    )
                    subcategories = DebitTransaction.SUBCATEGORY_CHOICES.get(
                        category, []
                    )
                    subcategory = (
                        random.choice(subcategories)[0] if subcategories else None
                    )
                    DebitTransaction.objects.create(
                        bank_account=bank_account,
                        transaction_name=fake.sentence(nb_words=3),
                        amount=round(random.uniform(10.00, 500.00), 2),
                        transaction_date=aware_dt,
                        category=category,
                        subcategory=subcategory,
                        is_recurring=random.choice([True, False]),
                        next_transaction_date=(
                            timezone.make_aware(fake.future_datetime())
                            if random.choice([True, False])
                            else None
                        ),
                        frequency=random.choice(["Monthly", "Weekly", "Yearly", None]),
                        description=fake.sentence(nb_words=6),
                    )

            # Create 1-2 financial goals for each user
            for _ in range(random.randint(1, 2)):
                goal_type = random.choice([g[0] for g in FinancialGoal.GOAL_TYPES])
                status = random.choice([s[0] for s in FinancialGoal.STATUS_CHOICES])
                priority = random.choice([p[0] for p in FinancialGoal.PRIORITY_CHOICES])
                frequency = random.choice(
                    [f[0] for f in FinancialGoal.FREQUENCY_CHOICES]
                )
                target_amount = round(random.uniform(500, 10000), 2)
                current_amount = round(random.uniform(0, target_amount), 2)
                target_date = fake.future_datetime(end_date="+1y")
                bank_account = (
                    random.choice(bank_accounts)
                    if bank_accounts and random.choice([True, False])
                    else None
                )

                FinancialGoal.objects.create(
                    user=user,  # user is a User instance from above
                    bank_account=bank_account,
                    goal_type=goal_type,
                    name=fake.sentence(nb_words=3),
                    description=fake.sentence(nb_words=6),
                    target_date=timezone.make_aware(target_date),
                    current_amount=current_amount,
                    target_amount=target_amount,
                    status=status,
                    priority=priority,
                    frequency=frequency,
                    is_recurring=(frequency != "One-time"),
                    is_completed=(status == "Completed"),
                )
