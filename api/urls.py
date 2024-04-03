from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
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
    name='book-gain-field-validation'
), path(
    'token/',
    obtain_auth_token,
    name='token'
), path(
    'forms/',
    views.IndicatorList.as_view(),
    name='gain-list'
), path(
    'gain/<int:indicator_id>/',
    views.IndicatorDetail.as_view(),
    name='gain-detail'
), path(
    'gain/validate-field/',
    views.IndicatorFieldValidation.as_view(),
    name='gain-field-validation'
)]

urlpatterns = format_suffix_patterns(
    urlpatterns
)
