# Genre Serializer
from rest_framework import serializers
from book_system.api.models import Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        exclude = ["created_by", "created", "modified_by", "modified", "is_active"]
