# Author Serializer
from rest_framework import serializers
from book_system.api.models import Author


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        exclude = ["created_by", "created", "modified_by", "modified", "is_active"]
