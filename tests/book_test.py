# Book Test
from django.test import TestCase
from django.db.models import Sum
from book_system.api.services import BookService


class BookTestCase(TestCase):
    def setUp(self):
        """There is no need to set up data"""

    def test_book_price_average(self):
        """Book price average have to be exactly the same amount"""
        year = 2024
        book_instance_list = BookService.get_by_year(year)
        book_total_number = int(book_instance_list.count())
        book_total_price = book_instance_list.aggregate(Sum("price"))

        if book_total_number == 0:
            book_total_number = 1

        book_average_price = book_total_price["price__sum"] / book_total_number

        service_book_average_price = BookService.get_avarage_price(year=year)

        self.assertEqual(
            book_total_number, service_book_average_price["number_of_books"]
        )
        self.assertEqual(
            book_average_price, service_book_average_price["average_price"]
        )
