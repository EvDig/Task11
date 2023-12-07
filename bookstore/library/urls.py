from django.urls import path, re_path

import library.views

app_name = "library"

urlpatterns = [
    path("add/", library.views.add_book, name="add_book"),
    path("from_to/", library.views.from_to, name="from_to"),
    path("file_upload/", library.views.file_upload, name="file_upload"),
    re_path(
        r"(?P<min_max_price>\w+)?",
        library.views.book_list,
        name="book_list",
    ),
]
