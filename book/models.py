from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.core.validators import MinValueValidator
from django.db import models


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

    PUBLISHERS = [('A', 'HACHETTE'), ('B', 'Flammarion'), ('C', 'ALBIN MICHEL'), ('D', 'GALLIMARD'),
                  ('E', 'LE LIVRE DE POCHE'), ('F', 'ROBERT LAFFONT'), ('G', 'J\'AI LU'), ('H', 'FAYARD')]

    publisher = models.CharField(
        max_length=1,
        choices=PUBLISHERS,
        default='A',
        help_text="L'éditeur du livre"
    )

    class Meta:
        permissions = {('view_hachette_book', 'Peut voir les livres de l\'éditeur Hachette'),
                       ('view_flammarion_book', 'Peut voir les livres de l\'éditeur Flammarion'),
                       ('view_albin_michel_book', 'Peut voir les livres de l\'éditeur Albin Michel'),
                       ('view_gallimard_book', 'Peut voir les livres de l\'éditeur Gallimard'),
                       ('view_le_livre_de_poche_book', 'Peut voir les livres de l\'éditeur Le Livre de Poche'),
                       ('view_robert_laffont_book', 'Peut voir les livres de l\'éditeur Robert Laffont'),
                       ('view_j_ai_lu_book', 'Peut voir les livres de l\'éditeur J\'ai Lu'),
                       ('view_fayard_book', 'Peut voir les livres de l\'éditeur Fayard')}
