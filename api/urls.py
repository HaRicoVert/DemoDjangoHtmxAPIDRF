from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [path(
    'books/',
    views.BookList.as_view(),
    name='book-list'
), path(
    'book/',
    views.BookDetail.as_view(),
    name='book-detail'
), path(
    'book/<int:book_id>/',
    views.BookDetail.as_view(),
    name='book-detail'
), path(
    'books/validate-field/',
    views.BookFieldValidation.as_view(),
    name='book-form-field-validation'
), ]

urlpatterns = format_suffix_patterns(
    urlpatterns
)
