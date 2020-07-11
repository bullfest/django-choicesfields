from django.db import models

from choicesfields import CharChoicesField, IntegerChoicesField, TextChoicesField
from . import constants


class ChoiceModel(models.Model):
    number = IntegerChoicesField(
        choice_type=constants.NumbersToCount, choices=constants.NumbersToCount.choices,
    )
    swallow_char = CharChoicesField(
        choice_type=constants.TypesOfSwallows, choices=constants.TypesOfSwallows.choices
    )
    swallow_text = TextChoicesField(
        choice_type=constants.TypesOfSwallows, choices=constants.TypesOfSwallows.choices
    )


class IntegerChoiceNullModel(models.Model):
    number = IntegerChoicesField(
        choice_type=constants.NumbersToCount,
        choices=constants.NumbersToCount.choices,
        null=True,
    )
    swallow_char = CharChoicesField(
        choice_type=constants.TypesOfSwallows,
        choices=constants.TypesOfSwallows.choices,
        null=True,
    )
    swallow_text = TextChoicesField(
        choice_type=constants.TypesOfSwallows,
        choices=constants.TypesOfSwallows.choices,
        null=True,
    )
