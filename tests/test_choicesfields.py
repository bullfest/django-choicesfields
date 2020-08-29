import pytest

from tests.test_app.constants import NumbersToCount
from tests.test_app.models import ChoiceModel


@pytest.mark.django_db
class TestIntegerChoices:
    def test_default(self):
        choice = ChoiceModel()
        choice.save()

        assert ChoiceModel.objects.count() == 1
        choice: ChoiceModel = ChoiceModel.objects.first()
        assert choice
        assert isinstance(choice.number, NumbersToCount)
        assert choice.number == NumbersToCount.ONE

    def test_assign_choice(self):
        choice = ChoiceModel(number=NumbersToCount.FIVE)
        choice.save()

        assert ChoiceModel.objects.count() == 1
        choice: ChoiceModel = ChoiceModel.objects.first()
        assert choice
        assert isinstance(choice.number, NumbersToCount)
        assert choice.number == NumbersToCount.FIVE

    def test_assign_int(self):
        choice = ChoiceModel(number=5)
        choice.save()

        assert ChoiceModel.objects.count() == 1
        choice: ChoiceModel = ChoiceModel.objects.first()
        assert choice
        assert isinstance(choice.number, NumbersToCount)
        assert choice.number == NumbersToCount.FIVE

    def test_save_illegal_int(self):
        choice = ChoiceModel(number=4)
        with pytest.raises(ValueError) as excinfo:
            choice.save()

        assert "4 is not a valid NumbersToCount" == str(excinfo.value)

    @pytest.mark.xfail(
        reason="This is the wanted behaviour, not sure how to implement yet."
    )
    def test_assign_illegal_int(self):
        with pytest.raises(ValueError) as excinfo:
            choice = ChoiceModel(number=4)

        assert "4 is not a valid NumbersToCount" == str(excinfo.value)

    @pytest.mark.xfail(
        reason="This is the wanted behaviour, not sure how to implement yet."
    )
    def test_assign_int_get_choice(self):
        choice = ChoiceModel(number=2)
        assert isinstance(choice.number, NumbersToCount)
        assert choice.number == NumbersToCount.TWO
