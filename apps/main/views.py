import subprocess

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def main(request):
    return render(request, "index.html")


@csrf_exempt
def ping_check(request):

    ping_search = request.body.decode("utf-8")

    if subprocess.call(["ping", "-c", "1", ping_search]) == 0:
        return JsonResponse({"server_ping": "yes"}, status=200)
    else:
        return JsonResponse({"server_ping": "no"}, status=200)
