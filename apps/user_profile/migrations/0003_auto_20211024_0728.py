# Generated by Django 3.1.3 on 2021-10-24 07:28
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0002_auto_20210911_1055"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="jwt_token",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]