from termcolor import cprint

from apps.monitoring.models import Monitor
from apps.monitoring.models import MonitorActivity
from apps.monitoring.models import Restore
from apps.monitoring.models import RestoreActivity


def ping(request, json_rq):
    ping = str(json_rq["ping"])

    print(ping)
    cprint(f"current user {request.user}", "cyan")
    cprint(f"current user.id {request.user.id}", "cyan")
    cprint(f"current profile.id {request.profile.id}", "cyan")
    cprint(f"current jwt token {request.jwt_token}", "cyan")
    cprint(f"request method {request.method}", "cyan")

    if True:
        return {"pong": ping}
    else:
        return {"error": "ping time out"}


def monitor_create(request, validated_data):

    monitor = Monitor()
    monitor.created_by = request.profile
    monitor.name = validated_data["monitor_name"]
    monitor.host = validated_data["monitor_host"]
    monitor.port = validated_data["monitor_port"]
    monitor.save()

    d = {}
    d["monitor_id"] = str(monitor.id)
    d["monitor_name"] = str(monitor.name)
    d["monitor_host"] = str(monitor.host)
    d["monitor_port"] = str(monitor.port)
    d["monitor_active"] = "no"
    d["monitor_last_monitoring_date"] = str(monitor.last_monitoring_date.strftime("%d.%m.%Y %H:%m") if monitor.last_monitoring_date else "")
    d["monitor_creation_date"] = str(monitor.creation_date.strftime("%d.%m.%Y") if monitor.creation_date else "")
    return {"monitor": d, "status": "added"}


def monitor_list(request, json_rq):
    monitors = []
    for monitor in Monitor.objects.filter(created_by=request.profile).order_by("id"):

        d = {}
        d["monitor_id"] = str(monitor.id)
        d["monitor_name"] = str(monitor.name)
        d["monitor_host"] = str(monitor.host)
        d["monitor_port"] = str(monitor.port)
        d["monitor_active"] = str("yes" if monitor.active else "no")
        d["monitor_last_monitoring_date"] = str(monitor.last_monitoring_date.strftime("%d.%m.%Y %H:%m") if monitor.last_monitoring_date else "")
        d["monitor_last_connection_establish"] = str("yes" if monitor.last_connection_establish else "no")
        d["monitor_last_response_time"] = str(monitor.last_response_time.strftime("%S.%f") if monitor.last_response_time else "")
        d["monitor_creation_date"] = str(monitor.creation_date.strftime("%d.%m.%Y") if monitor.creation_date else "")
        monitors.append(d)

    return {"monitors": monitors}


def monitor_view(request, validated_data):

    try:
        monitor = Monitor.objects.get(id=validated_data["monitor_id"])
        restore, created = Restore.objects.get_or_create(monitor=monitor)
    except:
        monitor = None

    if monitor:
        d = {}
        d["monitor_id"] = str(monitor.id)
        d["monitor_name"] = str(monitor.name)
        d["monitor_host"] = str(monitor.host)
        d["monitor_port"] = str(monitor.port)
        d["monitor_active"] = str("yes" if monitor.active else "no")
        d["monitor_last_monitoring_date"] = str(monitor.last_monitoring_date.strftime("%d.%m.%Y %H:%m") if monitor.last_monitoring_date else "")
        d["monitor_last_connection_establish"] = str("yes" if monitor.last_connection_establish else "no")
        d["monitor_last_response_time"] = str(monitor.last_response_time.strftime("%S.%f") if monitor.last_response_time else "")
        d["monitor_creation_date"] = str(monitor.creation_date.strftime("%d.%m.%Y") if monitor.creation_date else "")
        d["restore_host"] = str(restore.host or "")
        d["restore_port"] = str(restore.port or "")
        d["restore_username"] = str(restore.username or "")
        d["restore_password"] = str(restore.password or "")
        d["restore_commands"] = str(restore.commands or "")
        return {"monitor": d}
    else:
        return {"error": "No such monitor"}


def monitor_edit(request, validated_data):

    try:
        monitor = Monitor.objects.get(id=validated_data["monitor_id"])
    except:
        monitor = None

    if monitor:
        monitor.name = validated_data["monitor_name"]
        monitor.host = validated_data["monitor_host"]
        monitor.port = validated_data["monitor_port"]
        monitor.save()

        d = {}
        d["monitor_id"] = str(monitor.id)
        d["monitor_name"] = str(monitor.name)
        d["monitor_host"] = str(monitor.host)
        d["monitor_port"] = str(monitor.port)
        d["monitor_active"] = str("yes" if monitor.active else "no")
        d["monitor_last_monitoring_date"] = str(monitor.last_monitoring_date.strftime("%d.%m.%Y %H:%m") if monitor.last_monitoring_date else "")
        d["monitor_creation_date"] = str(monitor.creation_date.strftime("%d.%m.%Y") if monitor.creation_date else "")
        return {"monitor": d}
    else:
        return {"error": "Monitor has not been edited."}


def monitor_delete(request, validated_data):

    try:
        monitor_id = validated_data["monitor_id"]
    except:
        return {"error": "Monitor has not been found. Please input ID."}

    try:
        monitor = Monitor.objects.get(id=monitor_id)
    except:
        return {"error": "Monitor has not been deleted. Сouldn't find monitor with this ID=%s" % monitor_id}

    monitor.delete()
    return {"success": "Monitor successfully deleted. ID=%s" % monitor_id}


def monitor_start(request, validated_data):

    try:
        monitor_id = validated_data["monitor_id"]
    except:
        return {"error": "Monitor has not been found. Please input ID."}

    try:
        monitor = Monitor.objects.get(id=monitor_id)
    except:
        return {"error": "Monitor has not been deleted. Сouldn't find monitor with this ID=%s" % monitor_id}

    monitor.active = True
    monitor.save()

    return {"success": "Monitor successfully started. ID=%s" % monitor_id}


def monitor_stop(request, validated_data):

    try:
        monitor_id = validated_data["monitor_id"]
    except:
        return {"error": "Monitor has not been found. Please input ID."}

    try:
        monitor = Monitor.objects.get(id=monitor_id)
    except:
        return {"error": "Monitor has not been deleted. Сouldn't find monitor with this ID=%s" % monitor_id}

    monitor.active = False
    monitor.save()

    return {"success": "Monitor successfully stopped. ID=%s" % monitor_id}


def restore_edit(request, validated_data):

    try:
        monitor = Monitor.objects.get(id=validated_data["monitor_id"])
    except:
        monitor = None

    if monitor:

        restore, created = Restore.objects.get_or_create(monitor=monitor)
        restore.created_by = request.profile
        restore.host = validated_data["restore_host"]
        restore.port = validated_data["restore_port"]
        restore.username = validated_data["restore_username"]
        restore.password = validated_data["restore_password"]
        restore.commands = validated_data["restore_commands"]
        restore.save()

        d = {}
        d["monitor_id"] = str(monitor.id)
        d["monitor_name"] = str(monitor.name)
        d["monitor_host"] = str(monitor.host)
        d["monitor_port"] = str(monitor.port)
        d["monitor_active"] = str("yes" if monitor.active else "no")
        d["monitor_last_monitoring_date"] = str(monitor.last_monitoring_date.strftime("%d.%m.%Y %H:%m") if monitor.last_monitoring_date else "")
        d["monitor_creation_date"] = str(monitor.creation_date.strftime("%d.%m.%Y") if monitor.creation_date else "")

        return {"monitor": d}
    else:
        return {"error": "Monitor has not been edited."}


def monitor_activity(request, validated_data):

    try:
        monitor_id = validated_data["monitor_id"]
    except:
        return {"error": "Monitor has not been found. Please input ID."}

    monitor_activities = []
    for monitor_activity in MonitorActivity.objects.filter(monitor_id=monitor_id).order_by('id')[:30]:
        d = {}
        d["monitor_activity_id"] = str(monitor_activity.id)
        d["monitor_id"] = str(monitor_activity.monitor_id)
        d["monitor_connection_establish"] = str("yes" if monitor_activity.connection_establish else "no")
        d["monitor_monitoring_date"] = str(monitor_activity.creation_date.strftime("%d.%m.%Y %H:%M") if monitor_activity.creation_date else "")
        d["monitor_response_time"] = str(monitor_activity.response_time.strftime("%S.%f") if monitor_activity.response_time else "")
        d["monitor_response_time_ms"] = str(monitor_activity.response_time_ms if monitor_activity.response_time_ms else 0)
        d["monitor_creation_date"] = str(monitor_activity.creation_date.strftime("%d.%m.%Y %H:%M") if monitor_activity.creation_date else "")
        monitor_activities.append(d)

    return {"monitor_activities": monitor_activities}


def restore_activity(request, validated_data):

    try:
        monitor = Monitor.objects.get(id=validated_data["monitor_id"])
    except:
        return {"error": "Monitor has not been found. Please input ID."}

    restore_activities = []

    for restore_activity in RestoreActivity.objects.filter(restore__monitor=monitor)[:30]:
        d = {}
        d["restore_activity_id"] = str(restore_activity.id)
        d["restore_id"] = str(restore_activity.restore_id)
        d["restore_stdout_log"] = str(restore_activity.stdout_log if restore_activity.stdout_log else "")
        d["restore_stderr_log"] = str(restore_activity.stderr_log if restore_activity.stderr_log else "")
        restore_activities.append(d)

    return {"restore_activities": restore_activities}
