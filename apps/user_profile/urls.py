from django.urls import path

from apps.user_profile import views
from apps.user_profile.views import UserProfileView

app_name = "user_profile"

urlpatterns = [
    path("user-profile/", UserProfileView.as_view()),
    path("user-profile-post-avatar/", views.user_profile__post_avatar, name="user_profile__post_avatar"),
    path("user-profile-reset-api-key/", views.user_profile__reset_api_key, name="user_profile__reset_api_key"),
]
