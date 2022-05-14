import os
import sys

import ujson
from django.http import JsonResponse
from pydantic import BaseModel
from pydantic import Field
from pydantic import ValidationError
from simple_print import sprint
from termcolor import cprint

from settings import DEBUG


def error_response(request, error, status=400):
    if DEBUG:
        cprint(error, "red")
    return JsonResponse({"error": str(error)}, status=status)


class ErrorResponse(BaseModel):
    error_message: str = Field(description="Error message")


def validate_request_schema(request_schema):
    def wrap(func):
        def wrapped(request):

            if DEBUG:
                sprint(f"\n\n------- {func.__name__} -------", c="green", s=1, p=1)
                print(request.headers)
                print(request.body)
                print(request.method)

            try:
                request_body = request.body
                if not request_body:
                    request_body = "{}"

                json_rq = ujson.loads(request_body)
                json_rq = request_schema.validate(json_rq).dict()
                if DEBUG:
                    sprint(f"json_rq: {json_rq}", c="yellow", s=1, p=1)

                json_rs = func(request, json_rq)

                if hasattr(request, "is_test") and request.is_test:
                    return json_rs
                else:
                    return JsonResponse(json_rs, status=200)

            except ValidationError as error_message:
                if DEBUG:
                    sprint(f"{error_message}", c="red", s=1, p=1)

                return error_response(request, error_message, status=400)

            except Exception as error_message:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                full_error = f"{exc_type} {fname} {exc_tb.tb_lineno} {error_message}"
                if DEBUG:
                    sprint(f"{full_error}", c="red", s=1, p=1)
                return error_response(request, error_message)

        return wrapped

    return wrap
