from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models


def get_permissions_from_model():
    for model in models.get_models():
        content_type = ContentType.objects.get_for_model(
            model
        )
        for permission in model._meta.permissions:
            Permission.objects.get_or_create(
                codename=permission[0],
                content_type=content_type,
                name=permission[1]
            )
