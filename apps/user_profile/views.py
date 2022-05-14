import base64
import io
import uuid
from http.client import HTTPResponse
from json import JSONDecodeError

import psycopg2
from django.contrib.auth.models import User
from django.core.files.images import ImageFile
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from apps.mailer.mailer import Mailer
from apps.user_profile.decorators import auth_check
from settings import EXTERNAL_GATE__DATABASE_URL
from settings import PROJECT_MAIL


class UserProfileView(APIView):
    @csrf_exempt
    @method_decorator(auth_check())
    def get(self, request):

        try:
            username = request.user.username
            profile = request.profile
            email = request.user.email
            try:
                if request.profile.avatar and "static" not in request.profile.avatar:
                    avatar_url = request.profile.avatar
                else:
                    avatar_url = ""
            except:
                avatar_url = ""

            return JsonResponse(
                {
                    "message": "Success. Profile data received.",
                    "username": f"{username}",
                    "email": f"{email}",
                    "avatar_url": f"{avatar_url}",
                    "telegram_key": f"{profile.telegram_key}",
                    "secret_api_key": f"{profile.secret_api_key}",
                    "volume_mute": f"{profile.volume_mute}",
                },
                status=200,
            )
        except JSONDecodeError:
            return JsonResponse({"message": "Error. Can't parse json request. Profile data not received."}, status=400)

    @csrf_exempt
    @method_decorator(auth_check())
    def post(self, request):

        try:
            new_username = request.data.get("new_username")
        except Exception as e:
            new_username = None

        email = request.user.email
        user = User.objects.get(email=email)
        if user and new_username:
            user.username = new_username
            user.save()
            return JsonResponse({"message": "Success. User information has changed successfully.", "user_id": user.id}, status=200)
        else:
            return JsonResponse({"message": "Error. Unauthorized."}, status=401)

    @csrf_exempt
    @method_decorator(auth_check())
    def delete(self, request):

        try:
            email = request.user.email
        except JSONDecodeError:
            return JsonResponse({"message": "Can't parse json request."}, status=400)

        user = User.objects.get(email=email)
        user.delete()

        connection = psycopg2.connect(EXTERNAL_GATE__DATABASE_URL)
        cursor = connection.cursor()

        try:
            sql_update_query = f"""DELETE FROM public.user_user WHERE email='{email}';"""
        except JSONDecodeError:
            return JsonResponse({"message": "Can't find user email in database."}, status=400)

        cursor.execute(sql_update_query)
        connection.commit()

        cursor.close()
        connection.close()

        mailer_message = Mailer(
            sender=PROJECT_MAIL,
            recipient_list=(f"{email}"),
            subject="Your profile was deleted!",
            letter_body=f"Hello! Your profile was successfully deleted. You used this email:{email}. Thank you for using our service.",
        )
        mailer_message.send_email()

        return JsonResponse({"message": "User profile was deleted successfully."}, status=200)


@auth_check(wrap_dct={"profile": 1})
@csrf_exempt
def user_profile__post_avatar(request):

    payload = request.body.decode("utf-8")

    if "data:image/png" in payload and ";base64," in payload:
        payload = payload.replace("data:image/png;base64,", "")
        try:
            decoded_image = base64.b64decode(payload)
        except UnicodeDecodeError:
            JsonResponse({"message": "Invalid image. Can't decode base64."}, status=400)

        image_name = str(uuid.uuid4()) + ".png"
        email = request.user.email
        user = User.objects.get(email=email)
        new_avatar = ImageFile(io.BytesIO(decoded_image), name=image_name)

        if user:
            user.userprofile.avatar.save(image_name, new_avatar)
            return JsonResponse({"message": "User avatar has changed successfully.", "user_id": user.id}, status=200)
        else:
            return JsonResponse(
                {
                    "message": "Error. Unauthorized user.",
                },
                status=401,
            )
    else:
        return JsonResponse({"message": "Bad request. Wrong format. (need be 'data:image/png'"}, status=400)


@auth_check(wrap_dct={"profile": 1})
@csrf_exempt
def user_profile__reset_api_key(request):
    return HTTPResponse("OK")
