# Generated by Django 3.1.3 on 2021-02-14 08:50
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user_profile", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Monitor",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("host", models.CharField(max_length=255)),
                ("port", models.IntegerField(default=80)),
                ("active", models.BooleanField(default=True)),
                ("last_monitoring_date", models.DateTimeField(blank=True, null=True)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="user_profile.userprofile")),
            ],
        ),
        migrations.CreateModel(
            name="MonitorGroup",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="user_profile.userprofile")),
            ],
            options={
                "verbose_name": "Monitor group",
                "verbose_name_plural": "Monitor groups",
            },
        ),
        migrations.CreateModel(
            name="Restore",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("host", models.CharField(max_length=255)),
                ("port", models.IntegerField(default=80)),
                ("method", models.CharField(choices=[("GET", "GET"), ("POST", "POST"), ("PUT", "PUT"), ("DELETE", "DELETE"), ("PATH", "PATH")], default="GET", max_length=3000)),
                ("headers", models.CharField(blank=True, max_length=3000, null=True)),
                ("body", models.CharField(blank=True, max_length=3000, null=True)),
                ("query_params", models.CharField(blank=True, max_length=3000, null=True)),
                ("active", models.BooleanField(default=True)),
                ("restore_date", models.DateTimeField(blank=True, null=True)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="user_profile.userprofile")),
                ("monitor", models.ManyToManyField(blank=True, null=True, to="monitoring.Monitor")),
            ],
        ),
        migrations.CreateModel(
            name="RestoreActivity",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("stdout_log", models.TextField(blank=True, null=True)),
                ("stderr_log", models.TextField(blank=True, null=True)),
                ("creation_date", models.CharField(blank=True, max_length=255, null=True)),
                ("restore", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="monitoring.restore")),
            ],
        ),
        migrations.CreateModel(
            name="MonitorGroupRole",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("group_role", models.CharField(choices=[("administrator", "Administrator"), ("moderator", "Moderator"), ("viewer", "Viewer")], max_length=100)),
                ("group", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="monitoring.monitorgroup")),
                ("member", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="user_profile.userprofile")),
            ],
            options={
                "verbose_name": "Monitor group role",
                "verbose_name_plural": "Monitor group roles",
            },
        ),
        migrations.AddField(
            model_name="monitorgroup",
            name="members",
            field=models.ManyToManyField(related_name="monitor_group_member", through="monitoring.MonitorGroupRole", to="user_profile.UserProfile"),
        ),
        migrations.CreateModel(
            name="MonitorActivity",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("server_response", models.CharField(max_length=255)),
                ("response_time", models.TimeField()),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("monitor", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="monitoring.monitor")),
            ],
        ),
        migrations.AddField(
            model_name="monitor",
            name="monitor_group",
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="monitoring.monitorgroup"),
        ),
    ]