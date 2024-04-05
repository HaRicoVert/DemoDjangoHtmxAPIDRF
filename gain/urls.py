from django.urls import path

from gain import views

urlpatterns = [path(
    '',
    views.form,
    name='gain'
), path(
    'separated/',
    views.form_separated,
    name='gain_separated'
)]
