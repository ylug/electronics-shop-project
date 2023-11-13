"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import csv
import pytest

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
    with open('../src/items.csv') as file:
        read = csv.DictReader(file)
        assert read is not None
        for x in read:
            assert "name" in x
            assert "price" in x
            assert "quantity" in x


def test_string_to_number():
    assert Item.string_to_number('1') == 1


def test__repr__():
    assert repr(item1) == "Item('СмартфонСм', 2666.4, 3)"


def test__str__():
    assert str(item1) == 'СмартфонСм'


def test_instantiate_from_csv_file_not():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('nadir.csv')
