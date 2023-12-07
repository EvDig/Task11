import django.db.models

__all__ = ["BookManager"]


_all__ = []


class BookManager(django.db.models.Manager):
    def from_to(self, min_price, max_price):
        return self.get_queryset().filter(
            price__gte=min_price,
            price__lte=max_price,
        )
