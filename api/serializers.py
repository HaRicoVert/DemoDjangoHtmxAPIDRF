from rest_framework import serializers

from demo.models import Book
from form.models import Indicator


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
