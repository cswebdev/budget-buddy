from django.db import models
from bankaccounts.models import BankAccount


class DebitTransaction(models.Model):
    """
    This model is used to detail a user's bank account debit transaction(s).
    """

    # Main categories
    DEBIT_CATEGORIES = [
        ("Groceries", "Groceries"),
        ("Rent", "Rent"),
        ("Utilities", "Utilities"),
        ("Entertainment", "Entertainment"),
        ("Transportation", "Transportation"),
        ("Bills", "Bills"),
        ("Loans", "Loans"),
        ("Other", "Other"),
    ]

    SUBCATEGORY_CHOICES = {
        "Utilities": [
            ("Electricity", "Electricity"),
            ("Water", "Water"),
            ("Gas", "Gas"),
            ("Internet", "Internet"),
            ("Phone", "Phone"),
            ("Cable", "Cable"),
            ("Trash", "Trash"),
            ("Insurance", "Insurance"),
            ("Other", "Other"),
        ],
        "Entertainment": [
            ("Movies", "Movies"),
            ("Dining", "Dining"),
            ("Travel", "Travel"),
            ("Subscriptions", "Subscriptions"),
            ("Streaming", "Streaming"),
            ("Games", "Games"),
            ("Concerts", "Concerts"),
            ("Hobbies", "Hobbies"),
            ("Other", "Other"),
        ],
        "Transportation": [
            ("Gas", "Gas"),
            ("Public Transport", "Public Transport"),
            ("Parking", "Parking"),
            ("Tolls", "Tolls"),
            ("Maintenance", "Maintenance"),
            ("Insurance", "Insurance"),
            ("Other", "Other"),
        ],
        "Bills": [
            ("Credit Card", "Credit Card"),
            ("Mortgage", "Mortgage"),
            ("Student Loan", "Student Loan"),
            ("Personal Loan", "Personal Loan"),
            ("Car Loan", "Car Loan"),
            ("Other", "Other"),
        ],
        "Loans": [
            ("Student Loan", "Student Loan"),
            ("Personal Loan", "Personal Loan"),
            ("Car Loan", "Car Loan"),
            ("Mortgage", "Mortgage"),
            ("Other", "Other"),
        ],
        "Other": [
            ("Miscellaneous", "Miscellaneous"),
            ("Gifts", "Gifts"),
            ("Charity", "Charity"),
            ("Medical", "Medical"),
            ("Clothing", "Clothing"),
            ("Education", "Education"),
            ("Other", "Other"),
        ],}

    # Foreign key to the bank account model
    bank_account = models.ForeignKey(
        BankAccount, on_delete=models.CASCADE, related_name="debit_transactions"
    )

    # The name of the transaction
    transaction_name = models.CharField(max_length=255, default="Debit Transaction")

    # The amount of the transaction
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # The category of the transaction
    category = models.CharField(max_length=50, choices=DEBIT_CATEGORIES, default="Other")

    subcategory = models.CharField(max_length=50, blank=True, null=True)

    # Is the transaction recurring
    is_recurring = models.BooleanField(default=False)

    # The date of the next transaction
    next_transaction_date = models.DateTimeField(null=True, blank=True)

    # The frequency of the transaction
    frequency = models.CharField(max_length=50, null=True, blank=True)

    # The description of the transaction(optional)
    description = models.TextField(blank=True, null=True)

    # The date of the transaction
    transaction_date = models.DateTimeField()

    def __str__(self):
        return f"{self.bank_account} - {self.amount} - {self.transaction_date}"

    def get_subcategory_choices(self):
        """
        Returns the valid subcategory choices for the current category.
        """
        return self.SUBCATEGORY_CHOICES.get(self.category, [])
