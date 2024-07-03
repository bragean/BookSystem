# Genre Model
from .base_model import Base
from django.db.models import CharField


class Genre(Base):
    name = CharField(max_length=32, unique=True)
    code = CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name
