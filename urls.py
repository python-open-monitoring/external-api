from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path

# from apps.main import views as main_views


urlpatterns = [
    re_path(r"^", include("apps.main.urls")),
    re_path(r"^api/", include("apps.api.urls")),
    re_path(r"^user-profile/", include("apps.user_profile.urls", namespace="user_profile")),
]


urlpatterns += [
    path("admin/", admin.site.urls),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
