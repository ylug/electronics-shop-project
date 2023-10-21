import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, word):
        if len(word) >= 10:
            self.__name = word[:10]
        else:
            self.__name = word

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        cls.all = []
        path_part = path.split("/")
        path_file = os.path.join("..", path_part[0], path_part[1])
        with open(path_file, encoding='windows-1251', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for new in reader:
                name, price, quantity = dict.values(new)
                Item(name, price, quantity)

    @staticmethod
    def string_to_number(s: str):
        return int(float(s))
