from django.shortcuts import render

from api import views


# Create your views here.
def book_table_index(
    request
):
    return render(
        request,
        "apiview/book_table_index.html",
        context={
            "table_data_json": views.BookList().get(
                request
            ).data
        }
    )
