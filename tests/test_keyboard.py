import pytest
from src.keyboard import Keyboard


@pytest.fixture
def sample_keyboard():
    return Keyboard("Nadir_Keyboard", 15000.0, 1)


def test_creation_keyboard(sample_keyboard):
    assert sample_keyboard.quantity == 1
    assert sample_keyboard.price == 15000.0
    assert sample_keyboard.language == "EN"


def test_change_language(sample_keyboard):
    sample_keyboard.change_lang()
    assert sample_keyboard.language == "RU"
    sample_keyboard.change_lang()
    assert sample_keyboard.language == "EN"