from src.phone import Phone
from src.item import Item


def test_phone_creation():
    phone = Phone("Test Phone", 30000.0, 10, 1)
    item = Item("Test Model", 500, 5)
    assert phone.name == "Test Phone"
    assert phone.price == 30000.0
    assert phone.quantity == 10
    assert phone.number_of_sim == 1
    result = phone + item
    assert result == 15
