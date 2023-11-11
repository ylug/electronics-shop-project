import csv


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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity

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
    def instantiate_from_csv(cls, path='../src/items.csv'):
        try:
            cls.all = []
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                for line in reader:
                    item1 = (cls(line['name'], line['price'], line['quantity']))
                    cls.all.append(item1)
        except KeyError:
            raise InstantiateFromCsvError()
        except FileNotFoundError:
            return f"Отсутствует файл items.csv"

        def __add__(self, other):
            if not isinstance(other, Item):
                raise ValueError('Складывать можно только объекты Item и дочерние от них.')
            return int(self.quantity + other.quantity)

    @staticmethod
    def string_to_number(s: str):
        try:
            return int(s)
        except ValueError:
            s = s.split('.')
            return int(s[0])


class InstantiateFromCsvError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Файл items.csv повреждён"
