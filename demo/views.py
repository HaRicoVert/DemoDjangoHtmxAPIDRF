from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import (
    render,
    redirect,
)
from django.urls import reverse_lazy


@login_required()
def index(
    request
):
    return render(
        request,
        'demo/index.html'
    )


def form(
    request
):
    return render(
        request,
        'form/form.html'
    )


def test_input_validation(
    request
):
    return render(
        request,
        'demo/testInputValidation.html'
    )


def logout_view(
    request
):
    logout(
        request
    )
    return redirect(
        'index'
    )


class CustomLoginView(LoginView):
    template_name = 'demo/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

