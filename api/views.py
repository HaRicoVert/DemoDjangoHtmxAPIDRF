from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import BookSerializer
from demo.models import Book


class BookList(
    APIView
):
    def get(
        self,
        request,
        format=None
    ):
        books = Book.objects.all()
        serializer = BookSerializer(
            books,
            many=True
        )
        return Response(
            serializer.data
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
