from src.phone import Phone
import pytest


@pytest.fixture
def phone_1():
    return Phone("iPhone 14", 120_000, 5, 2)


def tests__str__(phone_1):
    assert str(phone_1) == 'iPhone 14'


def test__repr__(phone_1):
    assert repr(phone_1) == "Phone('iPhone 14', 120000, 5, 2)"


def number_of_sim(phone):
    assert phone.quantity_of_sim == 2
