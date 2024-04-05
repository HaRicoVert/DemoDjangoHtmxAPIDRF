from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(
    user_logged_in
)
def create_auth_token(
    sender,
    user,
    request,
    **kwargs
):
    Token.objects.get_or_create(
        user=user
    )
