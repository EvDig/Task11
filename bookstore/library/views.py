from django.contrib import messages
from django.shortcuts import redirect, render, reverse

import library.forms
import library.models

__all__ = []


def book_list(request, min_max_price="0_10**9"):
    try:
        prices = [float(i) for i in min_max_price.split("_")]
        min_price = prices[0]
        max_price = prices[1]

    except ValueError:
        min_price = 0.0
        max_price = float(10**9)

    template = "library/book_list.html"
    books = library.models.Book.objects.from_to(min_price, max_price)
    context = {"books": books}
    return render(request, template, context)


def add_book(request):
    template = "library/add_book.html"
    book_form = library.forms.BookForm(request.POST or None)
    if request.method == "POST" and book_form.is_valid():
        book_form.save(commit=True)
        messages.success(request, "Информация о книге сохранена!")
        return redirect(reverse("library:add_book"))

    context = {
        "form": book_form,
    }
    return render(request, template, context)


def from_to(request):
    template = "library/from_to.html"
    from_to_form = library.forms.FromToForm(request.POST or None)
    if request.method == "POST" and from_to_form.is_valid():
        data = from_to_form.cleaned_data
        min_price = data["min_price"]
        max_price = data["max_price"]
        return redirect(
            reverse("library:book_list") + f"{min_price}_{max_price}",
        )
    context = {
        "form": from_to_form,
    }
    return render(request, template, context)


def file_upload(request):
    template = "library/file_upload.html"
    file_upload_form = library.forms.FileUploadForm(request.POST or None)
    if request.method == "POST" and request.FILES:
        file = request.FILES["file"]
        lines = file.readlines()

        for line in lines:
            try:
                data = line.decode("ascii").rstrip().split()
                if float(data[4]) >= 0:
                    library.models.Book.objects.create(
                        name=data[0],
                        author=data[1],
                        publisher=data[2],
                        year=int(data[3]),
                        price=float(data[4]),
                    )
                else:
                    raise ValueError
            except (ValueError, IndexError):
                continue

        return redirect(reverse("library:book_list"))

    context = {
        "form": file_upload_form,
    }
    return render(request, template, context)
