from rest_framework import serializers

from book.models import Book
from gain.models import Indicator


class BookSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Book
        fields = '__all__'


class IndicatorSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Indicator
        fields = '__all__'
