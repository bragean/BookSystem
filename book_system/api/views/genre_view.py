# Genre View
from rest_framework.viewsets import ModelViewSet
from book_system.api.models import Genre
from book_system.api.serializers import GenreSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.filter(is_active=True)
    serializer_class = GenreSerializer
