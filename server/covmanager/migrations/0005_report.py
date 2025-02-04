# Generated by Django 1.11.16 on 2019-05-22 20:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("covmanager", "0004_reportconfiguration_reportsummary"),
    ]

    operations = [
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "data_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("public", models.BooleanField(default=False)),
                ("is_monthly", models.BooleanField(default=False)),
                ("is_quarterly", models.BooleanField(default=False)),
                (
                    "coverage",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="covmanager.Collection",
                    ),
                ),
            ],
        ),
    ]
