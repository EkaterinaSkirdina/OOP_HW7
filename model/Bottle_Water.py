from model.Product import Product


class Bottle_Water(Product):

    def __init__(self, name, price, volume) -> None:
        super().__init__(name, price, volume)

