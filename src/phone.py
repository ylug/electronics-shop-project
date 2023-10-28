from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def sim_p(self):
        if int(self.number_of_sim) != self.number_of_sim or self.number_of_sim <= 0:
            raise ValueError
