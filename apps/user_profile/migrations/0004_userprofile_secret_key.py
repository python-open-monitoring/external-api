# Generated by Django 3.1.3 on 2021-11-14 12:06
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0003_auto_20211024_0728"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="secret_key",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
