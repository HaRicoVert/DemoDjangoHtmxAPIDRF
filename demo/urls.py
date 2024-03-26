from django.urls import path

from demo import views

urlpatterns = [path(
    'index/',
    views.index,
    name='index'
), path(
    'form/',
    views.form,
    name='form'
), path(
    'forminputvalidation/',
    views.test_input_validation
), path(
    'logout/',
    views.logout_view,
    name='logout'
), path(
    'login/',
    views.CustomLoginView.as_view(),
    name='login'
)]
