# Generated by Django 3.1.3 on 2021-09-11 10:55
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="telegram_chat_id",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="telegram_key",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="profile_avatars/%Y/%m/%d"),
        ),
    ]
