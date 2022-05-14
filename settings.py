import os

from dotenv import load_dotenv

load_dotenv()

from pathlib import Path

DEBUG = os.getenv("DEBUG") == "1"
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_PREFIX = os.getenv("JWT_PREFIX")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
MAILJET_API_SECRET = os.getenv("MAILJET_API_SECRET")
MAILJET_API_KEY = os.getenv("MAILJET_API_KEY")
PROJECT_MAIL = os.getenv("PROJECT_MAIL")
EXTERNAL_GATE__DATABASE_URL = os.getenv("EXTERNAL_GATE__DATABASE_URL")

BASE_DIR = Path(__file__).resolve(strict=True).parent
SECRET_KEY = "8l6qik+u&*fttecup^8)9ca^71uo1yfz$$i)zsnlnfu4n9zu@b"


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "apps.api",
    "apps.monitoring",
    "apps.user_profile",
    "apps.main",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["drf_permissions.DrfApiPermission"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

ROOT_URLCONF = "urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
        "PASSWORD": POSTGRES_PASSWORD,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = True
