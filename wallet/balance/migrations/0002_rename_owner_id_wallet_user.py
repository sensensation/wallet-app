# Generated by Django 4.1.2 on 2022-12-05 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("balance", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="wallet",
            old_name="owner_id",
            new_name="user",
        ),
    ]