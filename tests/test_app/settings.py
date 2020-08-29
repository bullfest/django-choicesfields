"""
Dummy settings for test app
"""

SECRET_KEY = "supersecret"

INSTALLED_APPS = ["tests.test_app"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "CONN_MAX_AGE": 0,
        "NAME": ":memory:",
        "OPTIONS": {
            "timeout": 20,
        },
    }
}
