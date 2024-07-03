# Book View
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.response import Response
from book_system.api.models import Book
from book_system.api.serializers import BookSerializer
from book_system.api.services import BookService


class BookPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 10


class BookViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookSerializer
    pagination_class = BookPagination

    @action(methods=["GET"], detail=False)
    def get_avarage_price(self, request):
        year = request.query_params.get("year", None)

        if year is None:
            return Response(
                {"error": "el año es necesario"}, status=HTTP_400_BAD_REQUEST
            )

        average_price = BookService.get_avarage_price(year=year)

        return Response(average_price, status=HTTP_200_OK)
