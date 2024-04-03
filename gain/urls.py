from django.urls import path

from gain import views

urlpatterns = [path(
    '',
    views.form,
    name='gain'
)]
