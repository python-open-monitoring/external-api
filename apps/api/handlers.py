from django.views.decorators.csrf import csrf_exempt

from apps.api import methods
from apps.api import schema
from apps.api.helpers import validate_request_schema
from apps.user_profile.decorators import auth_check


@csrf_exempt
@auth_check(wrap_dct={"profile": 1})
@validate_request_schema(schema.Ping)
def ping(request, json_rq):
    return methods.ping(request, json_rq)


@csrf_exempt
@auth_check(wrap_dct={"profile": 1})
@validate_request_schema(schema.MonitorCreate)
def monitor_create(request, json_rq):
    return methods.monitor_create(request, json_rq)


@csrf_exempt
@auth_check(wrap_dct={"profile": 1})
@validate_request_schema(schema.MonitorList)
def monitor_list(request, json_rq):
    return methods.monitor_list(request, json_rq)


@csrf_exempt
@auth_check(wrap_dct={"profile": 1})
@validate_request_schema(schema.MonitorView)
def monitor_view(request, json_rq):
    return methods.monitor_view(request, json_rq)


@csrf_exempt
@auth_check(wrap_dct={"profile": 1})
@validate_request_schema(schema.MonitorEdit)
def monitor_edit(request, json_rq):
    return methods.monitor_edit(request, json_rq)


@csrf_exempt
@auth_check(wrap_dct={"profile": 1})
@validate_request_schema(schema.MonitorDelete)
def monitor_delete(request, json_rq):
    return methods.monitor_delete(request, json_rq)


@csrf_exempt
@auth_check(wrap_dct={"profile": 1})
@validate_request_schema(schema.MonitorStart)
def monitor_start(request, json_rq):
    return methods.monitor_start(request, json_rq)


@csrf_exempt
@auth_check(wrap_dct={"profile": 1})
@validate_request_schema(schema.MonitorStop)
def monitor_stop(request, json_rq):
    return methods.monitor_stop(request, json_rq)


@csrf_exempt
@auth_check(wrap_dct={"profile": 1})
@validate_request_schema(schema.MonitorActivity)
def monitor_activity(request, json_rq):
    return methods.monitor_activity(request, json_rq)


@csrf_exempt
@auth_check(wrap_dct={"profile": 1})
@validate_request_schema(schema.RestoreActivity)
def restore_activity(request, json_rq):
    return methods.restore_activity(request, json_rq)


@csrf_exempt
@auth_check(wrap_dct={"profile": 1})
@validate_request_schema(schema.RestoreEdit)
def restore_edit(request, json_rq):
    return methods.restore_edit(request, json_rq)
