from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import (
    HasViewPermission,
    HasViewFlammarionPermission,
    HasViewHachettePermission,
    HasViewAlbinMichelPermission,
    HasViewGallimardPermission,
    HasViewLeLivreDePochePermission,
    HasViewRobertLaffontPermission,
    HasViewJaiLuPermission,
    HasViewFayardPermission,
)
from api.serializers import (
    BookSerializer,
    IndicatorSerializer,
)
from demo.models import Book
from form.models import Indicator


class BookList(
    APIView
):
    permission_classes = [
        IsAdminUser | HasViewPermission | HasViewHachettePermission | HasViewFlammarionPermission | HasViewAlbinMichelPermission | HasViewGallimardPermission | HasViewLeLivreDePochePermission | HasViewRobertLaffontPermission | HasViewJaiLuPermission | HasViewFayardPermission]

    def get(
        self,
        request,
        format=None
    ):
        if request.user.is_superuser:
            books = Book.objects.all()
            return Response(
                BookSerializer(
                    books,
                    many=True
                ).data
            )

        permission_to_publisher = {
            'demo.view_hachette_book':          'A',
            'demo.view_flammarion_book':        'B',
            'demo.view_albin_michel_book':      'C',
            'demo.view_gallimard_book':         'D',
            'demo.view_le_livre_de_poche_book': 'E',
            'demo.view_robert_laffont_book':    'F',
            'demo.view_j_ai_lu_book':           'G',
            'demo.view_fayard_book':            'H'
        }

        # Initialiser une liste vide pour stocker les éditeurs autorisés
        allowed_publishers = []

        # Vérifier les permissions de l'utilisateur et ajouter les éditeurs autorisés à la liste
        for permission, publisher in permission_to_publisher.items():
            if request.user.has_perm(
                    permission
            ):
                allowed_publishers.append(
                    publisher
                )

        # Filtrer les livres en fonction des éditeurs autorisés
        books = Book.objects.filter(
            publisher__in=allowed_publishers
        )

        return Response(
            BookSerializer(
                books,
                many=True
            ).data
        )

    def post(
        self,
        request,
        format=None
    ):
        many = isinstance(
            request.data,
            list
        )

        serializer = BookSerializer(
            data=request.data,
            many=many
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_201_CREATED
            )
        else:
            errors = {}
            if errors:
                for key in serializer.errors.keys():
                    errors[key] = str(
                        serializer.errors[key][0]
                    )
                return Response(
                    errors,
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY
                )


class BookDetail(
    APIView
):
    def get(
        self,
        request,
        book_id: int,
        format=None
    ):
        try:
            book = Book.objects.get(
                id=book_id
            )
        except Book.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BookSerializer(
            book
        )
        return Response(
            serializer.data
        )

    def put(
        self,
        request,
        book_id: int,
        format=None
    ):
        try:
            book = Book.objects.get(
                id=book_id
            )
        except Book.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BookSerializer(
            book,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data
            )
        return Response(
            serializer.errors,
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    def delete(
        self,
        request,
        book_id: int,
        format=None
    ):
        try:
            book = Book.objects.get(
                id=book_id
            )
        except Book.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        book.delete()
        return Response(
            status=status.HTTP_200_OK
        )


class BookFieldValidation(
    APIView
):
    def post(
        self,
        request,
        format=None
    ):
        serializer = BookSerializer(
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            return Response(
                serializer.validated_data,
                status=status.HTTP_200_OK
            )
        else:
            errors = {}
            for key, value in serializer.errors.items():
                errors[key] = str(
                    value[0]
                )
            return Response(
                errors,
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )


class IndicatorList(
    APIView
):
    def get(
        self,
        request,
        format=None
    ):
        indicators = Indicator.objects.all()
        serializer = IndicatorSerializer(
            indicators,
            many=True
        )
        return Response(
            serializer.data
        )

    def post(
        self,
        request,
        format=None
    ):
        many = isinstance(
            request.data,
            list
        )

        serializer = IndicatorSerializer(
            data=request.data,
            many=many
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            errors = {}
            for key in serializer.errors.keys():
                errors[key] = str(
                    serializer.errors[key][0]
                )
            return Response(
                errors,
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )


class IndicatorDetail(
    APIView
):
    def get(
        self,
        request,
        indicator_id: int,
        format=None
    ):
        try:
            indicator = Indicator.objects.get(
                id=indicator_id
            )
        except Indicator.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = IndicatorSerializer(
            indicator
        )
        return Response(
            serializer.data
        )

    def put(
        self,
        request,
        indicator_id: int,
        format=None
    ):
        try:
            indicator = Indicator.objects.get(
                id=indicator_id
            )
        except Indicator.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = IndicatorSerializer(
            indicator,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data
            )
        return Response(
            serializer.errors,
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    def delete(
        self,
        request,
        indicator_id: int,
        format=None
    ):
        try:
            indicator = Indicator.objects.get(
                id=indicator_id
            )
        except Indicator.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        indicator.delete()
        return Response(
            status=status.HTTP_200_OK
        )


class IndicatorFieldValidation(
    APIView
):
    def post(
        self,
        request,
        format=None
    ):
        serializer = IndicatorSerializer(
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            return Response(
                serializer.validated_data,
                status=status.HTTP_200_OK
            )
        else:
            errors = {}
            for key, value in serializer.errors.items():
                errors[key] = str(
                    value[0]
                )
            return Response(
                errors,
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
