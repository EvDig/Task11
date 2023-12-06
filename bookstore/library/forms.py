import django.forms

from library.models import Book

__all__ = []


class BookForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Book
        fields = ["name", "author", "publisher", "year", "price"]

        labels = {
            "name": "Название книги",
            "author": "Автор",
            "publisher": "Издатель",
            "year": "Год издания",
            "price": "Цена",
        }
