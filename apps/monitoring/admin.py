from django.contrib import admin

from . import models


class MonitorAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "host",
        "port",
        "active",
        "last_monitoring_date",
        "created_by",
        "user_name",
        "creation_date",
    )
    list_filter = ("active",)
    search_fields = ("name",)

    def user_name(self, obj):
        return obj.created_by.user.email


class MonitorActivityAdmin(admin.ModelAdmin):

    list_display = ("id", "monitor", "connection_establish", "creation_date")
    list_filter = ("monitor",)


class RestoreAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "host",
        "port",
        "username",
        "password",
        "commands",
        "active",
        "restore_date",
        "created_by",
        "creation_date",
    )

    list_filter = ("active",)
    raw_id_fields = ("monitor",)
    search_fields = ("name",)


class RestoreActivityAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "restore",
        "stdout_log",
        "stderr_log",
        "creation_date",
    )
    list_filter = (
        "restore",
        "id",
        "restore",
        "stdout_log",
        "stderr_log",
        "creation_date",
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Monitor, MonitorAdmin)
_register(models.MonitorActivity, MonitorActivityAdmin)
_register(models.Restore, RestoreAdmin)
_register(models.RestoreActivity, RestoreActivityAdmin)
