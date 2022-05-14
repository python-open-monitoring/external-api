import os

from django.db import models

from apps.user_profile.models import UserProfile


def get_file_path(instance, filename):
    user_id = "%s" % instance.user_id
    file_name = filename.split(".")[0]
    file_ext = filename.split(".")[-1]
    filename = f"{file_name}.{file_ext}"
    return os.path.join(f"monitoring/{user_id}/{filename}")


class MonitorGroup(models.Model):
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(UserProfile, related_name="monitor_group_member", through="MonitorGroupRole")
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Monitor group"
        verbose_name_plural = "Monitor groups"


class MonitorGroupRole(models.Model):
    GROUP_ROLE_CHOICES = (
        ("administrator", "Administrator"),
        ("moderator", "Moderator"),
        ("viewer", "Viewer"),
    )
    member = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(MonitorGroup, on_delete=models.SET_NULL, null=True, blank=True)
    group_role = models.CharField(max_length=100, choices=GROUP_ROLE_CHOICES)

    def __str__(self):
        return f"{self.member} {self.group} {self.group_role}"

    class Meta:
        verbose_name = "Monitor group role"
        verbose_name_plural = "Monitor group roles"


class Monitor(models.Model):
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    monitor_group = models.ForeignKey(MonitorGroup, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    port = models.IntegerField(default=80)
    active = models.BooleanField(default=True)

    last_monitoring_date = models.DateTimeField(null=True, blank=True)
    last_connection_establish = models.BooleanField(null=True, blank=True)
    last_response_time = models.TimeField(null=True, blank=True)
    last_response_time_ms = models.IntegerField(null=True, blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.host}:{self.port}"


# post_save.connect(change_commands_syntax, sender=Monitor)


class MonitorActivity(models.Model):
    monitor = models.ForeignKey("monitoring.Monitor", on_delete=models.CASCADE)
    connection_establish = models.BooleanField(default=True)
    response_time = models.TimeField(null=True, blank=True)
    response_time_ms = models.IntegerField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.monitor} {self.server_response}"


class Restore(models.Model):

    monitor = models.ForeignKey("monitoring.Monitor", null=True, blank=True, on_delete=models.CASCADE)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)

    host = models.CharField(max_length=255, null=True, blank=True)
    port = models.IntegerField(null=True, blank=True)

    username = models.CharField(max_length=80, null=True, blank=True)
    password = models.CharField(max_length=80, null=True, blank=True)
    commands = models.CharField(max_length=8000, null=True, blank=True)

    active = models.BooleanField(default=True)
    restore_date = models.DateTimeField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.variable} {self.host}:{self.port}"


class RestoreActivity(models.Model):
    restore = models.ForeignKey("monitoring.Restore", on_delete=models.CASCADE)
    stdout_log = models.TextField(null=True, blank=True)
    stderr_log = models.TextField(null=True, blank=True)
    creation_date = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.restore}:{self.console_log}"
