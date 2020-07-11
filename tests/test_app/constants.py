from django.db import models


class NumbersToCount(models.IntegerChoices):
    ONE = 1, "One"
    TWO = 2, "Two"
    FIVE = 5, "Five"


class TypesOfSwallows(models.TextChoices):
    AFRICAN = "af", "African Swallow"
    EUROPEAN = "eu", "European Swallow"
