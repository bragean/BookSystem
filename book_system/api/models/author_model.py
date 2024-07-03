# Genre Model
from .base_model import Base
from django.db.models import CharField


class Author(Base):
    first_name = CharField(max_length=32)
    second_name = CharField(max_length=32)
    surname = CharField(max_length=32)
    second_surname = CharField(max_length=32)

    def __str__(self):
        return f"{self.first_name} {self.surname}"
