# Generated by Django 3.1 on 2020-08-29 08:56

import choicesfields
from django.db import migrations, models
import tests.test_app.constants


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChoiceModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    choicesfields.IntegerChoicesField(
                        choice_type=tests.test_app.constants.NumbersToCount, default=1
                    ),
                ),
                (
                    "swallow_char",
                    choicesfields.CharChoicesField(
                        choice_type=tests.test_app.constants.TypesOfSwallows,
                        default="af",
                        max_length=2,
                    ),
                ),
                (
                    "swallow_text",
                    choicesfields.TextChoicesField(
                        choice_type=tests.test_app.constants.TypesOfSwallows,
                        default="eu",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChoiceNullModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    choicesfields.IntegerChoicesField(
                        choice_type=tests.test_app.constants.NumbersToCount, null=True
                    ),
                ),
                (
                    "swallow_char",
                    choicesfields.CharChoicesField(
                        choice_type=tests.test_app.constants.TypesOfSwallows,
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "swallow_text",
                    choicesfields.TextChoicesField(
                        choice_type=tests.test_app.constants.TypesOfSwallows, null=True
                    ),
                ),
            ],
        ),
    ]