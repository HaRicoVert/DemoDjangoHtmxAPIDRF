from django.shortcuts import render


# Create your views here.

def index(
    request
):
    return render(
        request,
        'demo/index.html'
    )


def test(
    request
):
    return render(
        request,
        'demo/testtable.html'
    )


def test2(
    request
):
    return render(
        request,
        'demo/test.html'
    )


def book_table(
    request
):
    # On regarde les 
    return render(
        request,
        'demo/table.html'
    )
