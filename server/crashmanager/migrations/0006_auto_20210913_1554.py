# Generated by Django 2.2.20 on 2021-09-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crashmanager", "0005_user_notification_booleans"),
    ]

    operations = [
        migrations.AddField(
            model_name="bugzillatemplate",
            name="blocks",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="bugzillatemplate",
            name="dependson",
            field=models.TextField(blank=True),
        ),
    ]
