import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ApiConfig(AppConfig):
    name = "book_system.api"
    verbose_name = _("Api")

    def ready(self):
        with contextlib.suppress(ImportError):
            import book_system.api.signals  # noqa: F401
