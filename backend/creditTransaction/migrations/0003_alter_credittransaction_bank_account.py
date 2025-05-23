# Generated by Django 5.1 on 2025-05-21 02:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bankAccount", "0001_initial"),
        ("creditTransaction", "0002_credittransaction_transaction_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="credittransaction",
            name="bank_account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="credit_transactions",
                to="bankAccount.bankaccount",
            ),
        ),
    ]
