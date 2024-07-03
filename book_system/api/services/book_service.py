# Book Service
from book_system.api.serializers import BookPriceAverageSerializer
from book_system.api.models import Book
from django.db.models import Sum


class BookService():

    def get_avarage_price(year):
        book_instance = Book.objects.filter(published_date__year=year)
        average_price = book_instance.aggregate(Sum("price"))
        number_of_books = book_instance.count()

        book_price_average_serializer = BookPriceAverageSerializer(
            data={
                "average_price": (average_price["price__sum"] / number_of_books),
                "number_of_books": number_of_books,
                "year": year,
            }
        )
        book_price_average_serializer.is_valid(raise_exception=True)

        return book_price_average_serializer.data
