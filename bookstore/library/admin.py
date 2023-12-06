from django.contrib import admin

import library.models

__all__ = []

admin.site.register(library.models.Book)
