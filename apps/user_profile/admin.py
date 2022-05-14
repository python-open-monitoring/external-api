from django.contrib import admin

from . import models


class UserProfileAdmin(admin.ModelAdmin):

    list_display = ("id", "user_name", "avatar", "creation_date", "last_login_date", "volume_mute", "creation_date", "jwt_token")
    list_filter = ("creation_date",)
    search_fields = ("id",)

    def user_name(self, obj):
        return obj.user.email


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.UserProfile, UserProfileAdmin)
