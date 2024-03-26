from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
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
), path(
    'token/',
    obtain_auth_token,
    name='token'
)]

urlpatterns = format_suffix_patterns(
    urlpatterns
)
