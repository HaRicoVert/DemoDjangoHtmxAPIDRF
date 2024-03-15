from django.urls import path

from apiview import views

urlpatterns = [path(
    "book_table_index/",
    views.book_table_index,
    name="book_table_index"
)]
