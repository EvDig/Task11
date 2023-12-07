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


class FromToForm(django.forms.Form):
    min_price = django.forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        min_value=0,
        label="Минимальная цена",
    )
    max_price = django.forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        min_value=0,
        label="Максимальная цена",
    )


class FileUploadForm(django.forms.Form):
    file = django.forms.FileField(
        label="Файл",
        required=True,
    )
