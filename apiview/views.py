from datetime import datetime

from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)
from django.shortcuts import render

from api import views
from book.models import Book


@login_required
@permission_required(
    'book.view_book',
    raise_exception=True
)
def book_table_index(
    request
):
    # Récupération des données des livres à partir de la vue BookList
    book_list_data = views.BookList().get(
        request
    ).data

    # Transformation des données des livres en un format adapté pour le contexte
    table_data_json = []
    for book_data in book_list_data:
        formatted_book_data = {
            **book_data,
            'year':      datetime.strptime(
                book_data['year'],
                '%Y-%m-%d'
            ).date(),
            'publisher': dict(
                Book.PUBLISHERS
            ).get(
                book_data.get(
                    'publisher'
                )
            )
        }
        table_data_json.append(
            formatted_book_data
        )

    # Création du contexte pour le rendu de la page
    context = {
        "table_data_json": table_data_json
    }

    return render(
        request,
        "apiview/book_table_index.html",
        context
    )
