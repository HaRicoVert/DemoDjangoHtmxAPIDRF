from django.contrib import admin

from demo.models import Book


@admin.register(
    Book
)
class BookAdmin(
    admin.ModelAdmin
):
    list_display = ['title', 'author', 'price']
    list_filter = ['author']
