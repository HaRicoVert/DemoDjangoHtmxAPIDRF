from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Book(
    models.Model
):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text="Le titre du livre"
    )
    author = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text="L'auteur du livre"
    )
    year = models.DateField(
        null=False,
        blank=False,
        help_text="L'année de parution"
    )
    pages = models.IntegerField(
        null=False,
        blank=False,
        help_text="Le nombre de pages",
        validators=[MinValueValidator(
            1
        )]
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default="",
        null=True,
        blank=True,
        help_text="Le prix du livre",
        validators=[MinValueValidator(
            0
        )]
    )
