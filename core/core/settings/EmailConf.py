# region Email Conf
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = EMAIL_ACCOUNT  # type: ignore # noqa
EMAIL_HOST_PASSWORD = EMAIL_PASSWORD  # type: ignore # noqa

# endregion
