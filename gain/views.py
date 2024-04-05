from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from gain.forms import IndicatorForm


@login_required()
def form(
    request
):
    return render(
        request,
        'gain/index.html',
        context={
            'form': IndicatorForm()
        }
    )


@login_required()
def form_separated(
    request
):
    return render(
        request,
        'gain/index_separated.html',
        context={
            'form': IndicatorForm()
        }
    )
