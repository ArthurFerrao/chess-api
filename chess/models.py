from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError


class Piece(models.Model):
    COLOR_CHOICES = [
        ('black', 'Black'),
        ('white', 'White'),
    ]
    NAME_CHOICES = [
        ('king', 'King'),
        ('queen', 'Queen'),
        ('bishop', 'Bishop'),
        ('rook', 'Rook'),
        ('knight', 'Knight'),
        ('pawn', 'Pawn')
    ]

    name = models.CharField(max_length=50, choices=NAME_CHOICES)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)

    def __str__(self):
        return self.name + ' - ' + self.color


class Board(models.Model):
    rows = models.PositiveIntegerField(
        default=8,
        validators=[validators.MinValueValidator(1)]
    )
    columns = models.PositiveIntegerField(
        default=8,
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(26)
        ]
    )

    def save(self, *args, **kwargs):
        if not self.pk and Board.objects.exists():
            raise ValidationError(
                'There is can be only one Board instance')
        return super(Board, self).save(*args, **kwargs)

    def __str__(self):
        return 'rows: ' + str(self.rows) + ' | ' + 'columns: ' + str(self.columns)
