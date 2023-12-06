from django.contrib import messages
from django.shortcuts import redirect, render, reverse

import library.forms
import library.models

__all__ = []


def book_list(request):
    template = "library/book_list.html"
    books = library.models.Book.objects.all()
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
