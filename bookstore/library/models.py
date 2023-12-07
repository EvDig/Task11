import django.core.validators
import django.db.models

import library.managers

__all__ = []


class Book(django.db.models.Model):
    objects = library.managers.BookManager()

    name = django.db.models.CharField(
        verbose_name="название",
        max_length=33,
    )
    author = django.db.models.CharField(
        verbose_name="автор",
        max_length=33,
    )
    publisher = django.db.models.CharField(
        verbose_name="издательство",
        max_length=33,
    )
    year = django.db.models.IntegerField(
        verbose_name="год",
    )
    price = django.db.models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="цена",
        validators=[django.core.validators.MinValueValidator(0)],
    )

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"
