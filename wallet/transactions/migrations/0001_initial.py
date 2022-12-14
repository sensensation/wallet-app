# Generated by Django 4.1.2 on 2022-12-07 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("balance", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "transfer_amount",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("commision", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("success", "Success"),
                            ("fail", "Fail"),
                        ],
                        default="pending",
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "reciever",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reciever",
                        to="balance.wallet",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender",
                        to="balance.wallet",
                    ),
                ),
            ],
        ),
    ]
