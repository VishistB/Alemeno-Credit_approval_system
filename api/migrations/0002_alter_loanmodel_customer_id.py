# Generated by Django 4.2.8 on 2023-12-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loanmodel",
            name="customer_id",
            field=models.CharField(max_length=20),
        ),
    ]