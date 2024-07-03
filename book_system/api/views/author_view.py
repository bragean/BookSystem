# Author View
from rest_framework.viewsets import ModelViewSet
from book_system.api.models import Author
from book_system.api.serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.filter(is_active=True)
    serializer_class = AuthorSerializer
