# Book Serializer
from rest_framework import serializers
from book_system.api.models import Book
from rest_framework.serializers import DecimalField, IntegerField


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        exclude = ["created_by", "created", "modified_by", "modified", "is_active"]


class BookPriceAverageSerializer(serializers.Serializer):
    average_price = DecimalField(max_digits=8, decimal_places=2)
    year = IntegerField(min_value=0)
    number_of_books = IntegerField(min_value=0)