from django.urls import re_path

from apps.api import handlers

# monitor api
urlpatterns = (
    re_path(r"^ping/$", handlers.ping, name="ping"),
    re_path(r"^monitor/create/$", handlers.monitor_create, name="monitor_create"),
    re_path(r"^monitor/list/$", handlers.monitor_list, name="monitor_list"),
    re_path(r"^monitor/view/$", handlers.monitor_view, name="monitor_view"),
    re_path(r"^monitor/edit/$", handlers.monitor_edit, name="monitor_edit"),
    re_path(r"^monitor/delete/$", handlers.monitor_delete, name="monitor_delete"),
    re_path(r"^monitor/start/$", handlers.monitor_start, name="monitor_start"),
    re_path(r"^monitor/stop/$", handlers.monitor_stop, name="monitor_stop"),
    re_path(r"^restore/edit/$", handlers.restore_edit, name="restore_edit"),
    re_path(r"^monitor/activity/$", handlers.monitor_activity, name="monitor_activity"),
    re_path(r"^restore/activity/$", handlers.restore_activity, name="restore_activity"),
)
