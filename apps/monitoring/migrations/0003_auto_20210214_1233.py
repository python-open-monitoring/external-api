# Generated by Django 3.1.3 on 2021-02-14 12:33
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("monitoring", "0002_monitoractivity_connection_establish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="monitoractivity",
            name="server_response",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
