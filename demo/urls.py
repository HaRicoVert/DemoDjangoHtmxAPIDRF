from django.urls import path

from demo import views

urlpatterns = [path(
    'index/',
    views.index,
    name='index'
)]