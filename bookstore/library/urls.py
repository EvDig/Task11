from django.urls import path

import library.views

app_name = "library"

urlpatterns = [
    path("", library.views.book_list, name="book_list"),
    path("add/", library.views.add_book, name="add_book"),
]
