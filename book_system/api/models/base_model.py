# Base Model

import uuid
from django.db.models import Model, DateTimeField, UUIDField, BooleanField


class Base(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)
    created_by = UUIDField(editable=False, null=True)
    modified_by = UUIDField(editable=False, null=True)
    is_active = BooleanField(default=True)

    class Meta:
        abstract = True
