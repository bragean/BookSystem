# Book Service
from book_system.api.serializers import BookPriceAverageSerializer
from book_system.api.models import Book
from django.db.models import Sum


class BookService:

    def get_all():
        return Book.objects.filter(is_active=True)

    def get_by_year(year):
        return Book.objects.filter(is_active=True, published_date__year=year)

    def get_avarage_price(year):
        book_instance_list = BookService.get_by_year(year=year)
        book_total_price = book_instance_list.aggregate(Sum("price"))
        book_total_number = book_instance_list.count()

        if book_total_number == 0:
            book_total_number = 1
        
        print("gggg", book_total_price["price__sum"])

        book_price_average_serializer = BookPriceAverageSerializer(
            data={
                "average_price": (book_total_price["price__sum"]/book_total_number),
                "number_of_books": book_total_number,
                "year": year,
            }
        )
        book_price_average_serializer.is_valid(raise_exception=True)

        return book_price_average_serializer.data
