# Generated by Django 3.1.3 on 2021-02-14 11:52
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("monitoring", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="monitoractivity",
            name="connection_establish",
            field=models.BooleanField(default=True),
        ),
    ]
