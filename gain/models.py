from django.db import models


class Indicator(
    models.Model
):
    DOMAIN_CHOICES = (
        ("0", "DCIS"), ("1", "DCRFPN"), ("2", "DGPN"), ("3", "DCIS"), ("4", "DRCPN"), ("5", "Équipement et Logistique"),
        ("6", "Finances"), ("7", "Ressources humaines"), ("8", "SG/DRH"))
    domain = models.CharField(
        choices=DOMAIN_CHOICES,
        max_length=2
    )

    SECTOR_CHOICES = (
        ("0", "Accueil"), ("1", "Administration"), ("2", "Analyses et études"), ("3", "Armement"), ("4", "Budget"),
        ("5", "Cabinet"), ("6", "Communication"), ("7", "Contentieux"), ("8", "Audit"))
    sector = models.CharField(
        choices=SECTOR_CHOICES,
        max_length=2
    )

    FUNCTION_CHOICES = (("0", "Accueil physique et téléphonique"), ("1", "Audit, conseil et expertise"),
                        ("2", "Certification nationale"), ("3", "Communication internationale"),
                        ("4", "Coopération technique"), ("5", "Courier"), ("6", "Déroulements des cours"),
                        ("7", "Délivrance d'agréments"), ("8", "Entretiens de sécurité"), ("9", "Gestion des archives"))
    function = models.CharField(
        choices=FUNCTION_CHOICES,
        max_length=2
    )

    label = models.CharField(
        max_length=100,
        unique=True,
        help_text="Le libellé de l'indicateur"
    )

    INDICATOR_TYPE_CHOICES = (
        ("0", "Autre"), ("1", "BOP"), ("2", "Pilotage"), ("3", "DGPN"), ("4", "CG"), ("5", "PAP"), ("6", "UO"))
    indicator_type = models.CharField(
        choices=INDICATOR_TYPE_CHOICES,
        max_length=2
    )

    PERIOD_CHOICES = (("0", "Année"), ("1", "Semestre"), ("2", "Trimestre"), ("3", "Mois"))
    period = models.CharField(
        choices=PERIOD_CHOICES,
        max_length=2
    )

    description = models.TextField(
        null=True,
        blank=True,
        help_text="La description de l'indicateur"
    )

    detailed_entry = models.BooleanField(
        default=False,
        null=True,
        blank=True,
        help_text="L'entrée détaillée"
    )

    formula = models.TextField(
        help_text="La formule de calcul de l'indicateur"
    )
