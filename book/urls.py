from django.urls import path

from book import views

urlpatterns = [path(
    '',
    views.index,
    name='index'
), path(
    'logout/',
    views.logout_view,
    name='logout'
), path(
    'login/',
    views.CustomLoginView.as_view(),
    name='login'
)]
