# Generated by Django 4.1.2 on 2022-12-09 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("balance", "0002_alter_wallet_card_type"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="wallet",
            table="wallets",
        ),
    ]
