from django.shortcuts import render

from gain.forms import IndicatorForm


# Create your views here.
def form(
    request
):
    indicator_form = IndicatorForm()
    return render(
        request,
        'gain/form.html',
        context={
            'gain': indicator_form
        }
    )
