# Generated by Django 4.2.8 on 2023-12-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_loanmodel_loan_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="customermodel",
            name="age",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]