from django.contrib import admin
from django.contrib.auth.models import Permission

from book.models import Book
from gain.models import Indicator


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

admin.site.register(
    Indicator
)
