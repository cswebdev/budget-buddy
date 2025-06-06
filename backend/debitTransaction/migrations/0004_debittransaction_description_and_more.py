# Generated by Django 5.1 on 2025-05-22 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("debitTransaction", "0003_debittransaction_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="debittransaction",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="debittransaction",
            name="frequency",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="debittransaction",
            name="is_recurring",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="debittransaction",
            name="next_transaction_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="debittransaction",
            name="subcategory",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="debittransaction",
            name="category",
            field=models.CharField(
                choices=[
                    ("Groceries", "Groceries"),
                    ("Rent", "Rent"),
                    ("Utilities", "Utilities"),
                    ("Entertainment", "Entertainment"),
                    ("Transportation", "Transportation"),
                    ("Bills", "Bills"),
                    ("Loans", "Loans"),
                    ("Other", "Other"),
                ],
                default="Other",
                max_length=50,
            ),
        ),
    ]
