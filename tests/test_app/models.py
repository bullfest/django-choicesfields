from django.db import models

from choicesfields import CharChoicesField, IntegerChoicesField, TextChoicesField
from .constants import NumbersToCount, TypesOfSwallows


class ChoiceModel(models.Model):
    number = IntegerChoicesField(
        choice_type=NumbersToCount,
        default=NumbersToCount.ONE,
    )
    swallow_char = CharChoicesField(
        choice_type=TypesOfSwallows,
        max_length=2,
        default=TypesOfSwallows.AFRICAN,
    )
    swallow_text = TextChoicesField(
        choice_type=TypesOfSwallows,
        default=TypesOfSwallows.EUROPEAN,
    )


class ChoiceNullModel(models.Model):
    number = IntegerChoicesField(
        choice_type=NumbersToCount,
        null=True,
    )
    swallow_char = CharChoicesField(
        choice_type=TypesOfSwallows,
        max_length=2,
        null=True,
    )
    swallow_text = TextChoicesField(
        choice_type=TypesOfSwallows,
        null=True,
    )
