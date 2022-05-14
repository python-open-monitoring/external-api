import os
import uuid
from datetime import date

from django.contrib.auth.models import User
from django.db import models


def get_photo_path(instance, filename):
    today = date.today()
    ext = filename.split(".")[-1].lower()
    if ext == "":
        ext = "jpg"
    if not ext:
        ext = "jpg"
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("profile/", str(today.year), str(today.month), str(today.day), filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="profile_avatars/%Y/%m/%d", null=True, blank=True)
    volume_mute = models.BooleanField("Disable alerts sound", default=False)
    last_login_date = models.DateTimeField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    jwt_token = models.CharField(max_length=1000, null=True, blank=True)
    secret_api_key = models.CharField(max_length=1000, null=True, blank=True)
    telegram_key = models.CharField(max_length=255, null=True, blank=True)
    telegram_chat_id = models.IntegerField(null=True, blank=True)
