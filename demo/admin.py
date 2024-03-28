from django.contrib import admin
from django.contrib.auth.models import Permission

from demo.models import Book


@admin.register(
    Book
)
class BookAdmin(
    admin.ModelAdmin
):
    list_display = ['title', 'author', 'price']
    list_filter = ['author']


admin.site.register(
    Permission
)
