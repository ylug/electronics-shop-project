"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 3333, 3)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 9999


def test_apply_discount():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 2666.4


def test_name():
    item1.name = 'СмартфонСмартфон'
    assert item1.name == 'СмартфонСм'


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('1') == 1
