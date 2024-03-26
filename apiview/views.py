from datetime import datetime

from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)
from django.shortcuts import render

from api import views


@login_required
# @permission_required(
#     'demo.view_book',
#     raise_exception=True
# )
def book_table_index(
    request
):
    return render(
        request,
        "apiview/book_table_index.html",
        context={
            "table_data_json": [{
                **book_data,
                'year': datetime.strptime(
                    book_data['year'],
                    '%Y-%m-%d'
                ).date()
            } for book_data in views.BookList().get(
                request
            ).data]
        }
    )
