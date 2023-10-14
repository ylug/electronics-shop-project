"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 3333, 3)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 9999


def test_apply_discount():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 2666.4
