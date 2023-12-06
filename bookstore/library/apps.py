from django.apps import AppConfig

__all__ = ["LibraryConfig"]


class LibraryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "library"
    verbose_name = "библиотека"
