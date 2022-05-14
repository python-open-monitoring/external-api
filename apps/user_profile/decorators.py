import secrets
import uuid
from functools import wraps

import jwt
from django.contrib.auth.models import User
from django.http import JsonResponse
from simple_print import sprint

from apps.user_profile.models import UserProfile
from settings import DEBUG
from settings import JWT_ALGORITHM
from settings import JWT_PREFIX
from settings import JWT_SECRET_KEY


def auth_check(wrap_dct=None):
    def decorator(func):
        def inner_decorator(request, *args, **kwargs):
            sprint(f"auth_check decorator\n", c="red", b="on_white", s=1, p=1)
            sprint(request.headers)
            sprint(JWT_SECRET_KEY, JWT_PREFIX, JWT_ALGORITHM)
            if "Authorization" not in request.headers:
                return JsonResponse({"error": "Authorization header required"})

            authorization = str(request.headers["Authorization"])

            if ("MonitoringTestJwtToken__4rCTMAsKrKTB8rYz" in authorization) or (hasattr(request, "is_test") and request.is_test):
                jwt_token = authorization.split()[1]
                jwt_payload = {}
                jwt_payload["user_id"] = 1000
                jwt_payload["username"] = "Test user"
                jwt_payload["email"] = "test@test.test"

            else:
                if DEBUG:
                    sprint(f"JWT token from headers: {authorization}", c="cyan", s=1, p=1)

                try:
                    scheme, jwt_token = authorization.split()
                except ValueError:
                    if DEBUG:
                        sprint(f"Could not separate Authorization scheme and token", c="red", s=1, p=1)
                    return JsonResponse({"error": "Could not separate Authorization scheme and token"})

                if scheme.lower() != JWT_PREFIX.lower():
                    if DEBUG:
                        sprint(f"Authorization scheme {scheme} is not supported", c="red", s=1, p=1)
                    return JsonResponse({"error": f"Authorization scheme {scheme} is not supported"})

                try:
                    if DEBUG:
                        jwt_payload = jwt.decode(jwt_token, key=JWT_SECRET_KEY, algorithms=JWT_ALGORITHM, verify=False)
                    else:
                        jwt_payload = jwt.decode(jwt_token, key=JWT_SECRET_KEY, algorithms=JWT_ALGORITHM, verify=False)

                except jwt.InvalidTokenError:
                    if DEBUG:
                        sprint(f"Invalid JWT token {jwt_token}", c="red", s=1, p=1)
                    return JsonResponse({"error": "Invalid JWT token"})
                except jwt.ExpiredSignatureError:
                    if DEBUG:
                        sprint(f"Expired JWT token", c="red", s=1, p=1)
                    return JsonResponse({"error": "Expired JWT token"})

                if DEBUG:
                    sprint(f"Decoded JWT payload: {jwt_payload}", c="green", s=1, p=1)

            try:
                profile = UserProfile.objects.get(jwt_token=jwt_token)
                if False:
                    profile.telegram_key = secrets.token_urlsafe(32)
                    profile.save()
            except Exception as e:
                sprint("jwt token expired -> go to recreate", c="red", s=1, p=1)
                profile = None

            if not profile:

                try:
                    profile = UserProfile.objects.get(id=jwt_payload["user_id"])
                    if DEBUG:
                        profile.telegram_key = secrets.token_urlsafe(32)
                        profile.save()
                except Exception as e:
                    sprint(e, c="red", s=1, p=1)
                    profile = None

                if DEBUG:
                    sprint(f"Profile {profile}", c="green", s=1, p=1)

                if not profile:

                    try:
                        new_user = User.objects.create_user(username=jwt_payload["username"], email=jwt_payload["email"], password=f"{uuid.uuid4()}")
                        new_user.is_active = True
                        new_user.save()
                    except:
                        new_user = User.objects.get(email=jwt_payload["email"])

                    profile = UserProfile()
                    profile.id = profile.pk = jwt_payload["user_id"]
                    profile.telegram_key = secrets.token_urlsafe(32)
                    profile.user = new_user
                    profile.jwt_token = jwt_token
                    profile.save()

            request.profile = profile
            request.user = profile.user
            request.jwt_token = jwt_token

            return func(request, *args, **kwargs)

        return wraps(func)(inner_decorator)

    return decorator
