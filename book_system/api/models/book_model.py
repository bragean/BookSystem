# Book Model
from .base_model import Base
from .genre_model import Genre
from .author_model import Author
from django.db.models import (
    DateField,
    CharField,
    ForeignKey,
    CASCADE,
    DecimalField
)


class Book(Base):
    title = CharField(max_length=64, unique=True)
    price = DecimalField(max_digits=8, decimal_places=2)
    published_date = DateField()
    genre = ForeignKey(Genre, on_delete=CASCADE)
    author = ForeignKey(Author, on_delete=CASCADE)

    def __str__(self):
        return self.title
